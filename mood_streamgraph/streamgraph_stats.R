#Streamgraph will be used to show ratios for various statistics (mean, quartiles, etc) for valence and energy. 
#The different statistics will be stacked in each distribution.
#Valence will be on one side of the baseline (x-axis) and energy on the other.

#setwd("D:/immersion/spotify mood")
#devtools::install_github("hrbrmstr/streamgraph")
#install.packages("hablar")
library(dplyr)
library(tibble)
library(streamgraph)
library(lubridate)
library(readr)
library(hablar)
spmood1 <- read.csv(file= "combined_spmood.csv")
spmood1tib <- as_tibble(spmood1)
spmood1tib %>%
  convert(dte(Chart_Date))
