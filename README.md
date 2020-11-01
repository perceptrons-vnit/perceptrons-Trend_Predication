# Theme:3 Trendiness
## Table of Content
- [Overview](#Overview)
- [Objective](#Objective)
- [Procedure](#Procedure)
 *  [Trend Prediction](##Trend Prediction)
 *  [Semantic Segmentation](##Semantic Segmentation)
 *  [Attribute Recognition](##Attribute Recognition)
- [Installation](#Installation)
- [Results](#Results)

## Overview
Fast fashion has caused a massive increase in the rate at which new trends are set.

A lot of companies make replica of luxury products at an affordable price. 

As a result it is getting difficult for the average consumer to select apparels from such a vast variety. 

The problem is further elevated by the lack of interaction with the product which exists in traditional shopping, since it is difficult to choose a apparel without trial.
## Objective
With the rise of fast fashion, it is difficult to keep track of ever changing trends. 

A model that would help the user filter the products based on the latest trends will make the shopping experience a lot smoother and give Myntra an edge over other e-commerce sites.

Our model detects the latest trends in the market to help the user make the right choice. It would serve as each individual’s own personal, low budget stylist. 

The Virtual Trial Room will provide an easy and pleasant experience for any user.

## Procedure
### Trend Prediction
1. The first step includes collecting images from the popular social media site - Instagram.
- An account following some of the most famous fashion influencers of today is created.
- Instagram's algorithm ensures that the feed consists of posts in a descending order according to popularity.
- Making use of this feature of Instagram, a model - instagram_scraper1.py is created.
 The scraper model ( instagram_scraper1.py ) outputs - profile.txt, profiles.csv and datetime.csv.
 This shows us a detailed list of the profile names and the respective time stamps of posts appearing on the feed.
 
2. Next, run syntax.txt i.e. 

`instagram-scraper -f profile.txt -u perc.eptrons -p Myntra2020 --template {datetime}--latest-stamps time.txt`
in the command line.
> This downloads all the images after the particular latest time stamp. 

> time.txt contains the timestamps after which the images need to be downloaded.

> A folder containing all such images is created.

3. Run the notebook 'Save images.py'

> This compares the date time list with the csv files to obtain the required images and downloads them.

This completes the creation of basicdataset required for further steps.

### Semantic Segmentation

### Attribute Recognition
## Installation
## Results



An example of results obtained using open cv grabcut app:

<img src="https://user-images.githubusercontent.com/69817938/97804111-230a0300-1c67-11eb-92e6-f9fdeb224084.png" alt="Coat" width="250"/>









Our model wokrs in many parts :
  1. Srcaping from instragram the names and dates of relavent influencers for this we run instragram_scraper1.py, we then provide a proflie.txt to an open souce software which downloads images from instragram and saves in the relavent directory. We have made use of custom time stamps so that the open source software only downloads what is required. After that we select the appropriate images thorugh saveimages.py and save them in a dirctory.
    The open source software can be found on this Github repository: https://github.com/arc298/instagram-scraper
    `
