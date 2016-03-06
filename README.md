# spinupdown.py

This is a very simple tool that allows you to do one of two things:
1. Spin up a server from an image
2. Image a server (and delete it once complete)

## Installation

Installation is pretty easy:
* <touch .spinconfig>
* In <.spinconfig> add the following:
<[credentials]>
<RAX_USERNAME=your_username>
<RAX_API_KEY=your_api_key>
<RAX_REGION=your_datacenter>
* <pip install pyrax>

## Usage

* <python spinupdown.py>

Enjoy!
