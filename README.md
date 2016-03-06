# spinupdown.py

This is a very simple tool that allows you to do one of two things:
1. Spin up a server from an image
2. Image a server (and delete it once complete)

## Installation

Installation is pretty easy:
    $ vim .spinconfig

Add your credentials to the config cile
    RAX_USERNAME=your_username
    RAX_API_KEY=your_api_key
    RAX_REGION=your_preferred_datacenter

Also, make sure you have pyrax installed
    $ easy_install pip
    $ pip install pyrax

## Usage

    python spindownup.py

Enjoy!
