---
layout: post
title:  "Unity Save Game"
date: 2016-05-10
categories:
- programming
tags:
- programming
- game_design
- unity
---

When researching how to save data for the game I'm working on, I found a couple
solutions, namely Unity's built-in [PlayerPrefs][player-prefs] and the paid
plugin [Easy Save][easy-save]. However, I needed something more powerful than
PlayerPrefs and I couldn't justify spending $30 on Easy Save. Therefore, I
decided to implement my own save manager.

<!--more-->

[easy-save]: https://www.assetstore.unity3d.com/en/#!/content/768
[player-prefs]: https://docs.unity3d.com/ScriptReference/PlayerPrefs.html
[unity-persistence]: https://unity3d.com/learn/tutorials/modules/beginner/live-training-archive/persistence-data-saving-loading
