# An Instagram Downloader Wrapper
<div align="center">
<a href="#1"><img src="https://raw.githubusercontent.com/prabesharyal/ig_dlp/main/.github/ig_dlp.svg"/></a>
<br>
<img alt="GitHub Release Date - Published_At" src="https://img.shields.io/github/release-date/prabesharyal/ig_dlp">
<img alt="GitHub commit activity (branch)" src="https://img.shields.io/github/commit-activity/t/prabesharyal/ig_dlp">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/prabesharyal/ig_dlp">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/prabesharyal/ig_dlp">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/prabesharyal/ig_dlp">
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/prabesharyal/ig_dlp/total">
</div>

# Table of Contents
 1. [Introduction](#1)
    1. [About Module](#1.1)
	2. [Working Process](#1.2)
 2. [Get API key](#2)
 3. [Required Libraries](#3)
 4. [Usage](#4)
 5. [License](#lic)

# ig_dlp <a name="1"></a>
A kinda alternative of [yt-dlp](https://github.com/yt-dlp/yt-dlp) but for instagram.
>- Loader Animation credit : [StackOverFlow](https://stackoverflow.com/a/66558182/16370509)

## What is this mdoule about?<a name="1.1"></a>
This very simple Instagram Downloader module based on this [RapidAPI](https://rapidapi.com/maatootz/api/instagram-downloader-download-instagram-videos-stories) or [Cobalt](https://github.com/wukko/cobalt?tab=readme-ov-file) which helps you to download Instagram Posts, Videos and Stories in very simple way using python. You can Integrate this anywhere as you want. My implementation was this [telegram bot](https://github.com/prabesharyal/dalbhatpower_tg_bot). 

## How does this module work?<a name="1.2"></a>
> **This module works in various steps as :**
> - Requests the API
> - Parse Requied Data
> - Downloads
> - Returns required information as [here](#4).


# Rapid API Key<a name="2"></a>

You can get `X-RapidAPI-Key` from [Rapid API Site](https://rapidapi.com/maatootz/api/instagram-downloader-download-instagram-videos-stories)


> *Don't forget to set `X_RapidAPI_Key` value in the environment variable or in [.env](./.env) file.*


# Tools Required <a name="3"></a>

## Python <a name="3.1"></a>
Download Python From here :
> - [Python Latest Version](https://www.python.org/downloads/)

> *While installing, tick install **path / environment** variables whatever is given*

### Python Modules <a name="3.1.1"></a>
- **Install required python snippets using commands below:**
> - `pip install requests`
> - `pip install python-dotenv`

- _Install all other missing modules using :_
> - `pip install missing_module_name`

# Sample Usage <a name="4"></a>

Let's create a `downloader.py` in **same directory** as [this module](./insta_dlp.py). Then, the code for our downloader will be like this:
```
#Import our downloader function
from insta_dlp import Instagram_Downloader

url = input("Input Instagram Link : ")
check, caption, filelist = Instagram_Downloader(url)
if check != False:
    print("Identified Media Type: " + check)
    print("Post Caption : " + str(caption))
    print("Path of Downloaded Files: ", end ='')
    print(filelist)
else:
    print("Couldn't Download Instagram Post")

```

Type this command on terminal to run downloader:
>  `python3 downloader.py`

- Your Downloads will be saved in the directory list returned. If you had errors, it'll print them smoothly.


# License <a name="lic"></a>
> Distributed Under GPL by [@PrabeshAryalNP](https://facebook.com/prabesharyalnp) on [social](https://twitter.com/prabesharyalnp) or [@PrabeshAryal](https://github.com/prabesharyal) on code sites.
>-
>- Pushes and Commits on project are always welcome.

		
		
