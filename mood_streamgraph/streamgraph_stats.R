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
#Back to R

min_val <- read.csv("min_val.csv")
mc<- medcouple(min_val)
#-0.1538462
summary(min_val)
iqr_minv <- 0.06050-0.03970 
#medcouple <0 so whiskers are = to [Q1-1.5e^(-3MC)*IQR, Q3+1.5e^(4MC)*IQR]
#w1 <- .03970-1.5*exp(-3*mc)*iqr_minv 
#w2 <- 0.06050+1.5*exp(4*mc)*iqr_minv
minv_out <- adjOutl(min_val)
minv_out_arr <- grep("FALSE", minv_out$flagX)
#Outliers are 249 [9/5/19], 251-256 [9/7/19-9/12/19], 258-260 [9/14/19-9/16/19], 261-277 [9/17/19-10/3/19] [R indices, not Excel indices]--> HUMBLE by Kendrick Lamar

q1_val <- read.csv("q1_val.csv")
q1_val_out <- adjOutl(q1_val)
q1_val_out_arr <- grep("FALSE", q1_val_out_arr$flagX)
#No outliers

median_val <- read.csv("median_val.csv")
median_val_out <- adjOutl(median_val)
median_val_out_arr <- grep("FALSE", median_val_out_arr$flagX)
#No outliers

q3_val <- read.csv("q3_val.csv")
q3_val_out <- adjOutl(q3_val)
q3_val_out_arr <- grep("FALSE", q3_val_out$flagX)
#[359, 360- 12/24/19 & 12/25/19]

max_val <- read.csv("max_val.csv")
max_val_out <- adjOutl(max_val)
max_val_out_arr <- grep("FALSE", max_val_out$flagX)
#No outliers

min_energy_out <- adjOutl(min_energy)
min_energy_out <- adjOutl(min_energy)
#Error: A direction was found for which the robust scale estimate equals zero. See the help page for more details. 
min_energy_out_arr <- grep("TRUE", min_energy_out_arr$inSubspace)
#possibly can't be computed
#[1]  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  34
#[17]  35  36  40  41  42  43  54  55  56  57  65  81  82  89  90  91
#[33] 103 104 105 107 108 109 111 112 113 116 117 119 120 185 199 205
#[49] 206 207 227 244 246 247 248 249 295 312 317 318 319 323 324 325
#[65] 333 334 335 336 337 338 339 342 343 344 346 347 348 349 350 351
#[81] 352 353 354 355 356 357 358 359 360

q1_energy <- read.csv("q1_energy.csv")
q1_energy_out <- adjOutl(q1_energy)
q1_energy_out_arr <- grep("FALSE", q1_energy_out$flagX)
#12/24/19, 12/25/19

med_e <- read.csv("median_energy.csv")
med_e_out <- adjOutl(med_e)
med_e_out_arr <- grep("FALSE", med_e_out$flagX)
#No outliers

q3_energy <- read.csv("q3_energy.csv")
q3_energy_out <- adjOutl(q3_energy)
q3_energy_out_arr <- grep("FALSE", q3_energy_out$flagX)
#12/24/19, 12/25/19

max_energy <- read.csv("max_energy.csv")
max_energy_out <- adjOutl(max_energy)
max_energy_out_arr <- grep("FALSE", max_energy_out_arr$flagX)
#[1]  12  13  15  16  17  18  19  20  21  22  23  24  27  28  29  30
#[17]  31  32  33  34  35  36  37  38  40  41  42  44  45  46  47  48
#[33]  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64
#[49]  65  66  67 205 206 207 208 268 269 313 314 337



