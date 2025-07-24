# Pairs Trading in the Energy Sector

## The Energy Sector

The energy sector consists of companies involved in the production, distribution, and servicing of energy resources. This includes:

- Fossil Fuels
- Nuclear Energy
- Renewable Energy
- Infrastructure Companies
- Equipment Providers and Servicers


### Classification: GICS System

To understand the sector hierarchy, we use the Global Industry Classification Standard (GICS), developed by MSCI and S\&P in 1999. It is the most widely used system for classifying publicly traded equities worldwide.

#### GICS Hierarchy Table

| Level | Description | Example |
| :-- | :-- | :-- |
| Sector (2 digits) | Broad economic segment | 10 – Energy |
| Industry Group (4 digits) | Subdivision of sector | 1010 – Energy Equipment \& Services |
| Industry (6 digits) | More specific categorization | 101010 – Oil \& Gas Drilling |
| Sub-Industry (8 digits) | Most granular level | 10101010 – Offshore Drilling |

There are:

- 11 Sectors
- 24 Industry Groups
- 69 Industries
- 158 Sub-Industries


### Energy Sector GICS Breakdown

```
Sector 10: ENERGY
  ├── Industry Group 1010: Energy Equipment & Services
  │     ├── Industry 101010: Oil & Gas Drilling
  │     └── Industry 101020: Oil & Gas Equipment & Services
  └── Industry Group 101020: Oil, Gas & Consumable Fuels
        ├── Industry 10102010: Integrated Oil & Gas
        ├── Industry 10102020: Oil & Gas Exploration & Production
        ├── Industry 10102030: Oil & Gas Refining & Marketing
        ├── Industry 10102040: Oil & Gas Storage & Transportation
        └── Industry 10102050: Coal & Consumable Fuels
```

We will focus on 10102020 - Oil \& Gas Exploration and Production (E\&P).

## Oil Exploration \& Production Companies

These companies make up the upstream segment—the first link in the energy supply chain.


| Activity | Description |
| :-- | :-- |
| Exploration | Identify underground or underwater reserves using geological data, seismic surveys |
| Drilling | Deploy rigs to extract crude oil or natural gas |
| Production | Pump hydrocarbons from wells, bring to surface |
| Sale of Commodities | Sell crude oil and gas to midstream or refiners at spot or forward-linked prices |
| Hedging | Use derivatives to lock in future oil/gas prices for revenue certainty |

Revenue comes from selling crude oil and natural gas under benchmarks such as WTI, Brent Crude, and Henry Hub.

**Costs include:**

- CapEx: Drilling rigs, land leasing, seismic exploration
- OpEx: Labor, transport, compliance, water disposal
- Depletion: Non-renewable resources decline over time
- Hedging Costs: Cost of options/futures for price certainty


### Supply Chain Perspective

| Stage | GICS Sub-Industry Code | GICS Name | Example Role |
| :-- | :-- | :-- | :-- |
| Upstream | 10102020 | Oil \& Gas Exploration \& Production | E\&P firms (EOG, DVN, etc.) |
| Midstream | 10102040 | Oil \& Gas Storage \& Transportation | Pipelines, LNG terminals |
| Downstream | 10102030 | Oil \& Gas Refining \& Marketing | Refiners, retailers |

**Note:** E\&P firms locate reserves, drill, and produce oil/gas; they do not refine or transport it.

### Top E\&P Companies (Sub-Industry 10102020)

| Ticker | Company | Market Cap | Notes |
| :-- | :-- | :-- | :-- |
| EOG | EOG Resources | ~$75B | Diversified US shale giant |
| PXD | Pioneer Natural Resources | ~$60B (XOM) | Big Permian Basin player |
| FANG | Diamondback Energy | ~$40B | Permian-focused, efficient |
| DVN | Devon Energy | ~$30B | Large natural gas exposure |
| CTRA | Coterra Energy | ~$25B | Marcellus + Permian mixed |
| APA | APA Corp (Apache) | ~$12B | Africa + US focus |
| MUR | Murphy Oil | ~$8B | Offshore + onshore |
| SM | SM Energy | ~$6B | Mid-cap shale driller |
| MTDR | Matador Resources | ~$7B | Small cap, solid growth |
| AR | Antero Resources | ~$8B | Heavy natural gas/Appalachia |

### Why Cointegration Makes Sense in E\&P

| Reason | Implication |
| :-- | :-- |
| Common macro drivers (oil/natural gas) | Co-movement in fundamentals |
| Similar business models | Same revenue and cost drivers |
| Temporary divergence | Spread mean-reverts |
| ETF/flow-based pressure | Technical co-movement |
| Shared inputs (labor, land) | Structural cash flow linkage |

## Ticker Selection Criteria

Based on screening (e.g., Finviz):

1. Market Cap ≥ $2B
2. Volume > 300k
3. Price > $10
4. Sector: Energy; Industry: Oil \& Gas E\&P
5. Country: USA
6. Realistic PE Ratio > 0

**Selected Tickers:**

```python
tickers = [
    "COP",  # ConocoPhillips
    "EOG",  # EOG Resources
    "HES",  # Hess Corp
    "OXY",  # Occidental Petroleum
    "FANG", # Diamondback Energy
    "EQT",  # EQT Corp
    "DVN",  # Devon Energy
    "CTRA", # Coterra Energy
    "PR",   # Permian Resources
    "AR",   # Antero Resources
    "OVV",  # Ovintiv Inc
    "RRC",  # Range Resources
    "APA",  # APA Corporation
    "MTDR", # Matador Resources
    "CRK",  # Comstock Resources
    "CHRD", # Chord Energy
    "CNX",  # CNX Resources
    "MGY",  # Magnolia Oil & Gas
    "CRC",  # California Resources
]
```


## Beta and Beta Neutrality

### What is Beta?

Beta measures a stock's sensitivity to a factor (usually the market).

#### Formula:

$$
\beta = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}
$$

Where:

- $ R_i $: Stock return
- $ R_m $: Market return
- Cov, Var indicate covariance and variance

This quantifies how the stock moves with the market.

#### Regression Model:

$$
R_{\text{stock}} = \alpha + \beta \cdot R_{\text{market}} + \epsilon
$$

### Beta-Neutral Portfolios

You hedge so your net factor exposure is zero.

Suppose:

- Long Stock A $ (\beta_A = 1.2) $
- Short Stock B $ (\beta_B = 0.9) $

Net beta condition:

$$
\beta_{\text{net}} = w_A \cdot \beta_A - w_B \cdot \beta_B = 0
$$

Solving:

$$
\frac{w_A}{w_B} = \frac{\beta_B}{\beta_A}
$$

If $\beta_A = 1.2$, $\beta_B = 0.9$: $\frac{w_A}{w_B} = \frac{3}{4}$

So, long 3 units of A for every 4 units of B shorted.

### Pairs Trading and Beta Neutrality

Pairs trading targets cointegrated assets with mean-reverting spreads. But is the spread beta neutral?

#### Adjusted Spread Formula

$$
\text{Adjusted Spread} = \text{Original Spread} - w \cdot R_{\text{WTI}}
$$

Where:

- Original Spread: $ P_A - \beta \cdot P_B $
- $ w $: Hedge weight
- $ R_{WTI} $: WTI crude return


#### Is the Adjusted Spread Mean-Reverting?

By introducing a hedge, we get a three-leg spread. If the Johansen test confirms cointegration among $[P_A, P_B, \text{Hedge Asset}]$, the spread is still mean-reverting.

## Dynamic Hedging Strategy

1. **Hedge WTI Risk:**
Use CL=F (WTI futures), XOP, or similar oil ETFs.
2. **Careful Hedge Adjustment:**
Ensure stationarity is preserved but risk is lowered.
3. **Accept Minor Deviations:**
Slight deviations can improve PnL stability without sacrificing the core signal.

## Implementation Steps

Given the E\&P universe:

1. **ADF Test for the Spread:**

$$
S_t = P_A - \beta \cdot P_B
$$

Test if $ S_t $ is stationary (Augmented Dickey-Fuller test).
2. **Check WTI Exposure:**
Run regression:

$$
S_t \sim \gamma \cdot R_{\text{WTI}}
$$

If $ \gamma \neq 0 $: Spread has WTI exposure.
3. **Hedge and Re-Test:**
Add CL=F/XOP hedge and check for cointegration with the Johansen test.

## Key Formulas Recap

- **Original Spread:**
$ S_t = P_A - \beta \cdot P_B $
- **Adjusted Spread:**
$ Adj. Spread = S_t - w \cdot R_{WTI} $
- **WTI Exposure:**
$ S_t \sim \gamma \cdot R_{WTI} $
- **Beta Neutrality:**
$ \beta_{net} = w_A \cdot \beta_A - w_B \cdot \beta_B = 0 $
- **Johansen Test:**
Cointegration among $ P_A, P_B, Hedge Asset $


## Running on Your Local Machine

1. **Create Environment:**

```bash
conda env create -f environment.yml
conda activate energy-trading
```

2. **Register Kernel:**

```bash
python -m ipykernel install --user --name=energy-trading
```

