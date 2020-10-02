#Streamgraph will be used to show ratios for various statistics (mean, quartiles, etc) for valence and energy. 
#The different statistics will be stacked in each distribution.
#Valence will be on one side of the baseline (x-axis) and energy on the other.

#setwd("D:/immersion/spotify mood")
#devtools::install_github("hrbrmstr/streamgraph")
library(dplyr)
library(tibble)
library(streamgraph)
library(lubridate)
library(readr)
spmood1 <- read.csv(file= "combined_spmood.csv")
spmood1tib <- as_tibble(spmood1)
