#Streamgraph will be used to show ratios for various statistics (mean, quartiles, etc) for valence and energy. 
#The different statistics will be stacked in each distribution.
#Valence will be on one side of the baseline (x-axis) and energy on the other.
#4 streamgraphs for each quarterly period. Then radial graphs for interesting weeks.

#setwd("D:/immersion/spotify mood")
#devtools::install_github("hrbrmstr/streamgraph")
#install.packages("hablar")

#Make sure RTools is installed before doing this-- they're needed to build the GitHub package.
#install.packages("devtools")
#devtools::install_github("PSegaert/mrfDepth")

library(dplyr)
library(tibble)
library(streamgraph)
library(tidyverse)
library(lubridate)
library(readr)
library(hablar)
library(mrfDepth)
spmood1 <- read.csv(file= "combined_spmood.csv")
spmood1tib <- as_tibble(spmood1)
spmood1tib %>%
  #convert(dte(Chart_Date))
  as.POSIXct(format="%m/%d/%Y"))
spmood2tib <- spmood1tib %>%
  group_by(Chart_Date)%>%
  summarize(min_val=min(Valence),q1_val=quantile(Valence, .25),
  median_val=median(Valence),q3_val=quantile(Valence,.75),max_val=max(Valence), min_energy=min(Energy),q1_energy=quantile(Energy,.25),
  median_energy=median(Energy),q3_energy=quantile(Energy,.75),
  max_energy=max(Energy))

#Mutating in Excel to move data into 3 columns- value, key [type of statistic], and date
