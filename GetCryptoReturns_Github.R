# Define required packages
required_packages <- c("httr", "jsonlite", "tidyverse", "lubridate", "purrr")


# Check if packages are installed, install missing ones
install_if_missing <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, dependencies = TRUE)
  }
}


# Apply the function to each package
invisible(lapply(required_packages, install_if_missing))


# Load all packages
lapply(required_packages, library, character.only = TRUE)


# Function to get all available coin IDs from CoinGecko
get_all_coin_ids <- function() {
  url <- "https://api.coingecko.com/api/v3/coins/list"
  
  response <- GET(url)
  
  # Error handling
  if (http_error(response)) {
    stop("Failed to fetch data from CoinGecko API.")
  }
  
  # Parse response
  data <- content(response, "text") %>% fromJSON(flatten = TRUE)
  
  # Convert to a clean tibble
  coin_list <- tibble(
    id = data$id,
    symbol = toupper(data$symbol),  # Uppercase symbols for clarity
    name = data$name
  )
  
  return(coin_list)
}

# Fetch all coin IDs
all_coins <- get_all_coin_ids()

# Print first 10 results as preview
print(all_coins)


# Function to fetch historical prices in 90-day chunks
get_full_crypto_history <- function(coin_id, currency = "usd") {
  base_url <- "https://api.coingecko.com/api/v3/coins"
  all_data <- list()
  end_date <- Sys.Date()   # Start from today
  chunk_size <- 90         # Max days per API request
  
  repeat {
    start_date <- end_date - chunk_size  # Define start date for chunk
    url <- paste0(
      base_url, "/", coin_id, 
      "/market_chart/range?vs_currency=", currency, 
      "&from=", as.numeric(as.POSIXct(start_date)), 
      "&to=", as.numeric(as.POSIXct(end_date))
    )
    
    # Fetch data
    Sys.sleep(1)
    response <- GET(url)
    
    # Error handling for API request
    if (http_error(response)) {
      warning(paste("Failed to fetch data for", coin_id, "at", start_date))
      break
    }
    
    # Parse JSON response
    data <- content(response, "text") %>% fromJSON(flatten = TRUE)
    
    # Extract prices
    df <- tibble(
      coin = coin_id,
      timestamp = as_datetime(data$prices[, 1] / 1000),  # Convert from milliseconds
      price = data$prices[, 2],
      marketcap = data$market_caps[, 2]
      
    )
    
    # Store chunk
    #all_data <- append(all_data, df)
    all_data <- rbind(all_data, df)
    
    
    # Stop fetching if we hit earliest recorded date
    if (nrow(df) == 0 || min(df$timestamp, na.rm = TRUE) <= as.Date("2010-01-01")) {
      break
    }
    
    # Move to previous 90-day chunk
    end_date <- date(min(df$timestamp) - 1)
    
  }
  
  # Combine all chunks
  full_data <- bind_rows(all_data)
  
  # Re order by timestamp
  #full_data <- order(full_data$timestamp)
  full_data %>%
    arrange(timestamp)
  
  return(full_data)
}

# Function to compute daily log returns
compute_daily_returns <- function(price_data) {
  price_data %>%
    arrange(coin, timestamp) %>% # Ensure correct order
    group_by(coin) %>%
    mutate(return = log(price / lag(price))) %>%
    ungroup()
}

# Define coins to fetch
coins <- c("bitcoin", "ethereum", "solana")

# Loop through length of coins
for (i in 1:length(coins)) {
  # Fetch full historical data for all coins
  crypto_data <- get_full_crypto_history(tolower(coins[i]))
  
  # Compute daily returns
  crypto_returns <- compute_daily_returns(crypto_data)
  
  # Save the data
  write.csv(crypto_returns, 
            file = paste0("The\\Filepath\\",coins[i],"History.csv"))
  
  # Sleep to not hit API call limit
  Sys.sleep(60)
}
