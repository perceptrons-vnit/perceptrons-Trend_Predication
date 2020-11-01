# Theme:3 Trendiness
## Table of Contents
- [Overview](#Overview)
- [Objective](#Objective)
- [Procedure](#Procedure)
     *  [Trend Prediction](#Trend-Prediction)
     *  [Semantic Segmentation](#Semantic-Segmentation)
     *  [Attribute Recognition](#Attribute-Recognition)
- [Results](#Results)
- [Technologies Used](#Technologies-Used)

## Overview
Fast fashion has caused a massive increase in the rate at which new trends are set.

A lot of companies make replica of luxury products at an affordable price. 

As a result it is getting difficult for the average consumer to select apparels from such a vast variety. 

The problem is further elevated by the lack of interaction with the product which exists in traditional shopping, since it is difficult to choose a apparel without trial.
## Objective
With the rise of fast fashion, it is difficult to keep track of ever changing trends. 

A model that would help the user filter the products based on the latest trends will make the shopping experience a lot smoother and give Myntra an edge over other e-commerce sites.

Our model detects the latest trends in the market to help the user make the right choice. It would serve as each individual’s own personal, low budget stylist. 

### Trend Prediction
1. The first step includes collecting images from the popular social media site - Instagram.

- An account following some of the most famous fashion influencers of today is created.

- Instagram's algorithm ensures that the feed consists of posts in a descending order according to popularity.

- Making use of this feature of Instagram, a model - instagram_scraper1.py is created.

 The scraper model ( instagram_scraper1.py ) outputs -`profile.txt `,  `profiles.csv ` and  `datetime.csv `
 
 This shows us a detailed list of the profile names and the respective time stamps of posts appearing on the feed.
 
2. Next, run `syntax.txt` i.e. 

`instagram-scraper -f profile.txt -u perc.eptrons -p Myntra2020 --template {datetime}--latest-stamps time.txt`
in the command line.
> This downloads all the images after the particular latest time stamp. 

> time.txt contains the timestamps after which the images need to be downloaded.

> A folder containing all such images is created.

3. Run the notebook `saveimages.py` 

> This provides profile.txt to an open source software used by us, which downloads the images with the required custom time stamp with and saves them in a required directory.

The open source software can be found on this Github repository: https://github.com/arc298/instagram-scraper

This completes the creation of basic dataset required for further steps.

### Semantic Segmentation

Mask-RCNN is used to output segmented images or masks from the basic dataset created by us.

### Attribute Recognition

- A decoder-encoder model is used, the decoder being InceptionV3 model and encoder an LSTM-based model.

- The masks are fed to this model. The model grabs the images and classifies the pixels.

-  K- Means Classification is used for colour detection.

The final output of this prototype includes a list of the most trending colours and attributes for the user to choose from.

An interactive website is created by deploying the model using Flask.

## Results

A few examples of images obtained using the Mask-RCNN model for semantic segmentation are given below:

<img src="https://user-images.githubusercontent.com/69817938/97804111-230a0300-1c67-11eb-92e6-f9fdeb224084.png" width="250"/>
<img src="https://user-images.githubusercontent.com/73772990/97808699-c536e480-1c81-11eb-9492-3f99469a789c.png" width="250"/>
<img src="https://user-images.githubusercontent.com/73772990/97808735-fadbcd80-1c81-11eb-8690-e2fb88b963ca.png" width="250"/>


## Technologies Used

<img src="https://user-images.githubusercontent.com/73772990/97809284-67a49700-1c85-11eb-9e03-76dc3739f7d4.png" width="125"/>
<img src="https://user-images.githubusercontent.com/73772990/97809326-a20e3400-1c85-11eb-8aea-9d79449e2d15.png" width="100"/>
<img src="https://user-images.githubusercontent.com/73772990/97809354-ccf88800-1c85-11eb-9c25-71bee5b5f90d.png" width="100"/>
<img src="https://user-images.githubusercontent.com/73772990/97809388-fca79000-1c85-11eb-9798-615dd1871437.png" width="100"/>
<img src="https://user-images.githubusercontent.com/73772990/97809396-0df09c80-1c86-11eb-8e61-7bcaf68e15da.png" width="100"/>

