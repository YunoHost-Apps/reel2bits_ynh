# Reel2Bits for YunoHost

[![Integration level](https://dash.yunohost.org/integration/reel2bits.svg)](https://dash.yunohost.org/appci/app/reel2bits)  
[![Install Reel2Bits with YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=reel2bits)

> *This package allow you to install Reel2Bits quickly and simply on a YunoHost server.  
If you don't have YunoHost, please see [here](https://yunohost.org/#/install) to know how to install and enjoy it.*

## Overview
Soundcloud-like but simple, easy and KISS (and ActivityPub).

**Shipped version:** 0.0.1-2019-06-26

## Important points to read before installing

1. **Reel2Bits** is under development
1. **Reel2Bits** require a dedicated **root domain**, eg. reel2bits.domain.tld
1. Even if requested during installation: admin, language and password variables are not used
1. When your Reel2Bits instance is installed, you need to execute the following command to create a first user and give it admin rights: `(cd /var/www/reel2bits && ve3/bin/flask createuser)`

## Screenshots

![](https://user-images.githubusercontent.com/30271971/55600937-96335680-575e-11e9-947c-23fcfbd04715.PNG)

## Demo

* [Official demo](https://sound.otter.sh/user/dashie)

## YunoHost specific features

#### Supported architectures

* x86-64b - [![Build Status](https://ci-apps.yunohost.org/ci/logs/reel2bits%20%28Apps%29.svg)](https://ci-apps.yunohost.org/ci/apps/reel2bits/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/reel2bits%20%28Apps%29.svg)](https://ci-apps-arm.yunohost.org/ci/apps/reel2bits/)
* Jessie x86-64b - [![Build Status](https://ci-stretch.nohost.me/ci/logs/reel2bits%20%28Apps%29.svg)](https://ci-stretch.nohost.me/ci/apps/reel2bits/)

## Links

 * Report a bug: https://github.com/YunoHost-Apps/reel2bits_ynh/issues
 * Upstream app repository: https://github.com/rhaamo/reel2bits
 * YunoHost website: https://yunohost.org/

---

Developers info
----------------

Please do your pull request to the [testing branch](https://github.com/YunoHost-Apps/reel2bits_ynh/tree/testing).

To try the testing branch, please proceed like that.
```
sudo yunohost app install https://github.com/YunoHost-Apps/reel2bits_ynh/tree/testing --debug
or
sudo yunohost app upgrade reel2bits -u https://github.com/YunoHost-Apps/reel2bits_ynh/tree/testing --debug
```
