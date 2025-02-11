# Diary of a Caravaneer

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Trading System](#trading-system)
- [Inventory System](#inventory-system)
- [Mission System](#mission-system)
- [Contributing](#contributing)
- [License](#license)

### Overview
**Diary of a Caravaneer** is a trade and economic simulator RPG game developed in Ren'Py. Players take on the role of a merchant traveling with their son and daughter through a world on the brink of chaos. The goal is to earn enough money to escape to Vaelris before the outbreak of the Balenvhenian Scramble. The game combines mechanics of buying and selling, managing a food cart, and interacting with the family.

#### Platform
- PC

#### Engine
- Ren'Py

#### Genre
- Trading and management simulation with RPG elements

#### Objectives
- Create a gameplay experience that blends the satisfaction of economic management with a heartwarming narrative about family.
- Offer a medium-length gameplay experience, between 15-20 hours.
- Stand out with its pixel art style and setting in a world on the brink of war.
- Implement a dynamic and engaging trading system, with realistic market fluctuations.

#### Gameplay Pillars
- **Strategic Trading**: Buying and selling goods should be the core of the game, with the need to research markets for optimal profits.
- **Food Cart Micro-Management**: Preparing and selling food is a secondary mechanic to earn additional income, with an ingredient combination system and drink service.
- **Personal Narrative**: The player will experience an emotional story about a family seeking a better future in a changing world.

#### Narrative
The game is set in the fictional world of Balen Saga, in the time before the Balenvhenian Scramble, a period of unrest and political tensions. The protagonist, a traveling merchant, seeks a better future for their family away from the dangers of war. The main objective is to gather funds to travel to Vaelris, a promised land of safety.

#### Target Market
- **Age**: 15-50
- **Preferences**: Gamers who appreciate an emotional narrative and strategic management, and who enjoy relaxing and cozy games.

#### Highlighted Competitors
- Stardew Valley
- Moonlighter
- Travellers Rest


### Project Structure

The project is made using Ren'Py. The current plugins implemented into the project are:
- [AutoHighlight](https://wattson.itch.io/renpy-auto-highlight)


### Trading System

- [Overview of the Trading System](#trading-system-overview)
- [Trading System Formulas](#trading-system-formulas)

#### Trading System Overview

The game aims to have a close-to real medieval trading experience. 

- Each store has the variables of **StoreGold**, **"StoreType"** and **"StoreEconomicPower"**
  - Each item per-store has a **"BaseStock"**, **"RestockTimer"**, **"RestockAmount"**
- Each location has **"LocationEconomicPower"**
  - Each item per-location has a variable of **"ItemDemand"** 
 
The buy price and sell price of each item is determined by a complex formula that aims to simulate that realistic medieval trading experience. 

A store can't buy items from the player if they don't have enough StoreGold to buy it.

When a player buys an item, the stock gets reduced by the amount that the player bought (if the amount reaches 0 then the player can't buy that specific item from that specific shop until the stock is back to higher than 0), and the location economic power variable increases by the price of the item sold multiplied by 1% (With a maximum of 100), and the location demand of the item increases in proportion of how many items are left in the stock vs the base stock value (the higher the difference between items, the higher the demand value, with a maximum value of 100). 

The store type affects the type of items a store accepts to buy from the player (The items sold by the store are determined through code), and the store economic power starts at a base value and increases or decreases through random hidden events, modifiers and mainly through player interaction, as the power increases as the player buys items from a store, and decreases when the store buys items from the player. Then we do some formulas hidden from the player to simulate the store handling that inventory to determine an outcome: The store "sells the items succesfully" and the store economic power returns to normal, or the store "fails to sell the items" and their power returns proportionally to how successful or unsuccessful they were. Store Gold might seem like a duplicate variable of Store Economic Power, but the Gold value means the cash liquidity of the store, so the real relation is that the Store Gold value is directly proportionate to the Store Economic Power. 

Additionally, the buy and sell final prices are affected by the Item Demand, as the amount of items in stock in proportion at the base stock at a specific location proportionally affects the demand of said item at that location. So, if Cragbrook has a high demand for Wood, the stores that handle Wood will buy Wood at a higher price, and also sell it at a higher price. The item demand of each city per location also have a permanent variable and a dynamic variable to effectively simulate if a location is actually a producer of that item, like Cragbrook is a producer of stone, and to simulate if there's a global modifier like a "Massive Request for Salt" which affects the prices globally.

#### Trading System Formulas

The Buy formula is: TBD

The Sell formula is: TBD

Store Gold formula: TBD

Store Economic Power formula: TBD

Location Economic Power formula: TBD

Item Demand formula: TBD


The sell price of an item can't be higher than the buy price of that same item in that same store. This works as the motivator for players to rotate around locations, buying items where they are cheap and selling them where they are expensive. 


### Inventory System




