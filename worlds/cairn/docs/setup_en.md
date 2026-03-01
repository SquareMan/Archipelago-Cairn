# Cairn Archipelago Setup Guide

## Required Software

- [Cairn](https://store.steampowered.com/app/1588550/Cairn/)
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases/latest)
- [CairnAp](https://codeberg.org/TheCoolSquare/CairnAp)
  - Requires [This MelonLoader Fork](https://github.com/SquareMan/MelonLoader)
- [This apworld](https://github.com/SquareMan/Archipelago)

## Where are the locations?

Currently all the implemented locations are "Loot Providers". This includes the loose single items you can pick up as well as each individual slot in loot containers.
For location accessibility reasons, all loot for a container will be guaranteed to spawn, ignoring any conditions such as game difficulty or current items.

Note that the Vending Machines at the starting of the game in the Tenzen climbing gym are NOT locations. These have an infinite stock of items and will still give you
what you pay for if you manage to find any coins before leaving.

## Connecting to a Server

At the moment while server information must be passed on the commandline before launching the game. The relevant arguments are
1. `--CairnAp.hostname <hostname>`
2. `--CairnAp.port <port>`
3. `--CairnAp.slot <slot>`

One way of supplying these arguments is with a steam protocol url. For example, if you run this in a terminal:

`start steam://run/1588550//--CairnAp.hostname%20archipelago.gg%20--CairnAp.port%2038281%20--CairnAp.slot%20Square`

Steam will launch Cairn by first popping up a confirmation window showing the non-standard command line options.

Note that `1588550` is the Steam App ID of Cairn and the `%20`s are spaces separating the arguments

Once in game, there is a Connect button in the top level corner that can be clicked at any time.

## Starting a game

The game can be started at any time before or after the server is connected to. Received items are persisted to the save file so the game can be restarted or reloaded at any point.
It is recommened for now to play on Alpinist difficulty. Other difficulties should work but at the moment you will run into some issues with some locations not being reachable.
The only thing to be aware of is that locations checked while disconnected from the server are not yet persisted to save file so if the game is restarted before reconnected they will be missed.
