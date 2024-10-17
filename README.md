# Real-Time Weather Monitoring System

## Overview

The Real-Time Weather Monitoring System is a Python application that continuously retrieves weather data from the OpenWeatherMap API, processes the data, and provides summarized insights, including daily weather summaries, temperature rollups, and alerting mechanisms based on configurable thresholds. The system is designed to monitor weather conditions in major metros in India, including Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Key Configuration](#api-key-configuration)
- [Processing and Analysis](#processing-and-analysis)
- [Test Cases](#test-cases)
- [Bonus Features](#bonus-features)
- [License](#license)

## Features

- **Real-time Data Retrieval**: Automatically retrieves weather data from the OpenWeatherMap API every 5 minutes.
- **Temperature Conversion**: Converts temperature from Kelvin to Celsius based on user preferences.
- **Daily Weather Summary**: Calculates daily aggregates including:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- **Alerting Mechanism**: Notifies users when weather conditions exceed user-defined thresholds.
- **Data Visualization**: Displays historical trends and daily summaries.

## Technologies

- Python 3.x
- Requests library for API calls
- SQLite or any other database for persistent storage (optional)
- Optional libraries for data visualization (e.g., Matplotlib, Seaborn)

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/WeatherMonitoring.git
