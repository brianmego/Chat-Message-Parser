********************************
**  CHAT PARSER DOCUMENTATION
**  Updated: 5/27/2014
**  Latest Update: Brian Mego
********************************


********************************
**  Overview
********************************
    This chat parser takes input in the form of chat messages that might be seen on twitter, then
    parses the metadata into mentions, emoticons, and links. Any part of the message that is not
    qualified as metadata will be ignored.


********************************
**  Getting Setup
********************************
    After this repo is cloned, here's the checklist to get everything set up and ready to scrape:

    1. Ensure Python is installed on the machine (Python 2.7.5+ 64 bit supported)
    2. Read this http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip/
       (you can ignore the section on Fabric)
    3. Setup a virtualenv if this is not the only python development on your machine (virtualenv 1.10+ supported)
    4. cd to the root of this repo and run "python setup.py"
    5. run "nosetests" from the root of this repo ensure everything installed correctly*
