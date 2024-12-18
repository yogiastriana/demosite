comments = """
1. Error Handling and Debugging
   - Dict keys: `error`, `messages`, `stacktraces`
   - Explanation: These keys are used to track and report errors or issues during the execution of the portfolio optimization process. They ensure that if something goes wrong (e.g., data issues or computation errors), you can trace it back and understand what happened. This helps in debugging and ensuring robust model operation.
   - Task: Internal purposes for now

2. Covariance and Correlation
   - Dict keys: `covariance`, `correlation`
   - Explanation: Indicates the directional relationship between two assets
   - Task: Create heatmaps for both

3. Efficient Frontier and Frontier Runs
   - Dict keys: `frontier_runs`, `frontier_runs.x`, `frontier_runs.y`
   - Explanation: The efficient frontier represents the set of optimal portfolios offering the highest expected return for a defined level of risk. The x and y values represent risk (e.g., standard deviation) and return, respectively. These are used in mean-variance optimization to visualize the trade-off between risk and return for different portfolio compositions
   - Task: Plot a graph

4. Symbol Portfolios
   - Dict keys: `symbol_portfolios`
   - Explanation: This group holds key data for each individual asset in the portfolio
   - Task: Create tables

5. Stats: Descriptive Statistics
   - Dict keys: `stats_descriptive`
   - Explanation: Descriptive statistics of asset/portfolio's behavior
   - Task: Create tables 

6. Stats: Moments
   - Dict keys: `stats_moments`
   - Explanation: These higher-order moments describe the distribution of asset/portfolio returns
   - Task: Create tables 

7. Stats: Risk Measures
   - Dict keys: `stats_risk_measures`
   - Explanation: These are measures of risk specific to each asset/portfolio
   - Task: Create tables 

8. Stats: Ratios
   - Dict keys: `stats_ratios`
   - Explanation: These ratios help to assess the risk-adjusted performance of asset/portfolio
   - Task: Create tables 

9. Strategy Results
   - Dict keys: `strategy_results`
   - Explanation: This group contains the performance of different portfolio strategies

9. Strategy Result Data
   - Dict keys:
	   - `performance`: Performance metrics
	   - `weights`: Target allocation of each asset in the strategy
	   - `position`: Position in efficient frontier graph (x, y)
	   - `summary`: Stats summary (`stats_moments`, `stats_risk_measures`, `stats_ratios`, `strategy_results`)
	   - `symbol_contribution_summary`: Contribution of each symbol to stats summary
	   - `allocation`: Actual allocation
	   - `allocation_summary`: Summary of the allocation
	   - `extra_measures`: Additional measures
	   - `ticker_contribution_extra_measures`: Contribution of each symbol to additional measures
   - Task: Create tables of performance, others will be used later 
"""

model_output_data = {
    "error": False,
    "messages": None,
    "stacktraces": None,
    "covariance": {
        "AAPL": {
            "AAPL": 1.809088571722628,
            "CSCO": 0.8810707374913874,
            "NFLX": 1.1961454157805718,
            "AMD": 1.6953426539746628,
            "CVX": 0.7248801398576267,
            "PFE": 0.4625337443748518,
            "MMM": 0.6462425399012145,
            "MSFT": 1.3087545752333423
        },
        "CSCO": {
            "AAPL": 0.8810707374913874,
            "CSCO": 1.402176377896002,
            "NFLX": 0.6113313629908689,
            "AMD": 1.08338049649089,
            "CVX": 0.7609370044453041,
            "PFE": 0.5364987987794271,
            "MMM": 0.6877467375050406,
            "MSFT": 0.859235460362977
        },
        "NFLX": {
            "AAPL": 1.1961454157805718,
            "CSCO": 0.6113313629908689,
            "NFLX": 3.7555005216183375,
            "AMD": 1.8307196386167908,
            "CVX": 0.36177867750924364,
            "PFE": 0.30311205961779075,
            "MMM": 0.4699679994262865,
            "MSFT": 1.2052109471112842
        },
        "AMD": {
            "AAPL": 1.6953426539746628,
            "CSCO": 1.08338049649089,
            "NFLX": 1.8307196386167908,
            "AMD": 4.551840627887994,
            "CVX": 0.838816987948787,
            "PFE": 0.49374367407811776,
            "MMM": 0.7174404311498549,
            "MSFT": 1.7200718074995862
        },
        "CVX": {
            "AAPL": 0.7248801398576267,
            "CSCO": 0.7609370044453041,
            "NFLX": 0.36177867750924364,
            "AMD": 0.838816987948787,
            "CVX": 2.360129357656256,
            "PFE": 0.5028195855370107,
            "MMM": 0.7860789714382003,
            "MSFT": 0.6841140546689412
        },
        "PFE": {
            "AAPL": 0.4625337443748518,
            "CSCO": 0.5364987987794271,
            "NFLX": 0.30311205961779075,
            "AMD": 0.49374367407811776,
            "CVX": 0.5028195855370107,
            "PFE": 1.3103430281113093,
            "MMM": 0.4522723167675434,
            "MSFT": 0.4906481986726891
        },
        "MMM": {
            "AAPL": 0.6462425399012145,
            "CSCO": 0.6877467375050406,
            "NFLX": 0.4699679994262865,
            "AMD": 0.7174404311498549,
            "CVX": 0.7860789714382003,
            "PFE": 0.4522723167675434,
            "MMM": 1.342077272233804,
            "MSFT": 0.5747689501451212
        },
        "MSFT": {
            "AAPL": 1.3087545752333423,
            "CSCO": 0.859235460362977,
            "NFLX": 1.2052109471112842,
            "AMD": 1.7200718074995862,
            "CVX": 0.6841140546689412,
            "PFE": 0.4906481986726891,
            "MMM": 0.5747689501451212,
            "MSFT": 1.6975163081228424
        }
    },
    "correlation": {
        "AAPL": {
            "AAPL": 100.0,
            "CSCO": 33.63369325939919,
            "NFLX": 49.29063218959222,
            "AMD": 75.7147708944929,
            "CVX": -21.989038554855032,
            "PFE": -51.660676184927155,
            "MMM": -24.520818343703528,
            "MSFT": 87.98240489986546
        },
        "CSCO": {
            "AAPL": 33.63369325939919,
            "CSCO": 100.0,
            "NFLX": -13.873205101192912,
            "AMD": 35.97779700232235,
            "CVX": 3.5708206066085784,
            "PFE": -30.430040146246597,
            "MMM": 2.7187909952877387,
            "MSFT": 32.670862362499896
        },
        "NFLX": {
            "AAPL": 49.29063218959222,
            "CSCO": -13.873205101192912,
            "NFLX": 100.0,
            "AMD": 48.2998550292033,
            "CVX": -42.24929418286648,
            "PFE": -49.60119158671203,
            "MMM": -39.24791613298523,
            "MSFT": 52.98431709674774
        },
        "AMD": {
            "AAPL": 75.7147708944929,
            "CSCO": 35.97779700232235,
            "NFLX": 48.2998550292033,
            "AMD": 100.0,
            "CVX": -15.090434847836082,
            "PFE": -34.32222312097006,
            "MMM": -14.785627509092894,
            "MSFT": 80.15526642588351
        },
        "CVX": {
            "AAPL": -21.989038554855032,
            "CSCO": 3.5708206066085784,
            "NFLX": -42.24929418286648,
            "AMD": -15.090434847836082,
            "CVX": 100.0,
            "PFE": -14.235654008205275,
            "MMM": 25.732199609858963,
            "MSFT": -25.41568415279344
        },
        "PFE": {
            "AAPL": -51.660676184927155,
            "CSCO": -30.430040146246597,
            "NFLX": -49.60119158671203,
            "AMD": -34.32222312097006,
            "CVX": -14.235654008205275,
            "PFE": 100.0,
            "MMM": -31.16613218703671,
            "MSFT": -47.47764370350455
        },
        "MMM": {
            "AAPL": -24.520818343703528,
            "CSCO": 2.7187909952877387,
            "NFLX": -39.24791613298523,
            "AMD": -14.785627509092894,
            "CVX": 25.732199609858963,
            "PFE": -31.16613218703671,
            "MMM": 100.0,
            "MSFT": -32.95490533044114
        },
        "MSFT": {
            "AAPL": 87.98240489986546,
            "CSCO": 32.670862362499896,
            "NFLX": 52.98431709674774,
            "AMD": 80.15526642588351,
            "CVX": -25.41568415279344,
            "PFE": -47.47764370350455,
            "MMM": -32.95490533044114,
            "MSFT": 100.0
        }
    },
    "frontier_runs": {
        "x": [
            0.21396877543019466,
            0.2140109058042823,
            0.21411315785495832,
            0.21427547510661388,
            0.21449761714198792,
            0.21477944165052487,
            0.2151207523992265,
            0.2155212186427888,
            0.21598056537870539,
            0.21649839870585857,
            0.21707423347483473,
            0.21770770631077152,
            0.21839820603570773,
            0.21914531922082398,
            0.21994838370332306,
            0.22080682504287588,
            0.22171997169111504,
            0.22268441984784235,
            0.22369485511191792,
            0.22475059492274901,
            0.2258510086284457,
            0.22699544494373455,
            0.2281832314460498,
            0.2294137104597035,
            0.23068617615099468,
            0.23199997543195766,
            0.23335434255742865,
            0.23474865207303425,
            0.2361822108334722,
            0.23765707323614085,
            0.23917408950772645,
            0.2407322645726766,
            0.2423309847953326,
            0.24396940594012498,
            0.24564672301912915,
            0.24736722234274475,
            0.24915151280400963,
            0.2510007728899506,
            0.2529133395768671,
            0.25488797358880744,
            0.25692321490477554,
            0.2590176440047239,
            0.26116980406314694,
            0.263378282374313,
            0.2656417049159671,
            0.26795865906843735,
            0.2703277039540944,
            0.272747594853752,
            0.2752170067436623,
            0.27773446410318114,
            0.2802987710648868,
            0.28290865544717014,
            0.2855628661526544,
            0.2882601570247731,
            0.2909993392300766,
            0.29377932023566933,
            0.29659880065260064,
            0.299456706560398,
            0.3023520288721022,
            0.30528369740339784,
            0.3082505874183079,
            0.3112642383011306,
            0.31437241717180453,
            0.3175820924157811,
            0.3208901557823575,
            0.3242934148162599,
            0.3277891200706332,
            0.33137415315164,
            0.3350458301136055,
            0.3388012587727118,
            0.3426376847720797,
            0.3465524258280255,
            0.3505428401202604,
            0.3546162168422404,
            0.3588012411664623,
            0.36322686735728854,
            0.3679105325027492,
            0.37284250645547107,
            0.3780130278731248,
            0.3834124821017607,
            0.38903130294999444,
            0.3948601757782389,
            0.4008899180895347,
            0.40711154137678585,
            0.4135164739026706,
            0.42009640501352397,
            0.4268429604181025,
            0.4337486285980119,
            0.440805846620907,
            0.44800755383596474,
            0.45534668790063376,
            0.46281673248765726,
            0.47041162175156853,
            0.4781253165760255,
            0.4859521595147633,
            0.4938868470804114,
            0.5019241175950708,
            0.5100591530102729,
            0.5182874329652623,
            0.526604545413548
        ],
        "y": [
            0.08937998553070665,
            0.09375791982149606,
            0.09814302320540647,
            0.10252874022355096,
            0.10691384145523972,
            0.11129884191468324,
            0.11568414136782394,
            0.12006940657781533,
            0.12445473168767321,
            0.12884007020873967,
            0.1332252847831701,
            0.13761059509095194,
            0.141995820257202,
            0.14638115487407716,
            0.15076641764915694,
            0.15515170529889874,
            0.15953692103598474,
            0.16392222973698936,
            0.1683074941258982,
            0.17269276573977047,
            0.177078053285855,
            0.18146335643619005,
            0.18584862231864832,
            0.19023393604920663,
            0.19461919478145084,
            0.19900453367468335,
            0.2033897429756287,
            0.20777504642477448,
            0.21216033397965683,
            0.2165456098785978,
            0.22093095878279326,
            0.22531617238701646,
            0.22970145119211943,
            0.23408673095003904,
            0.2384720050571102,
            0.24285729027613098,
            0.24724257028382957,
            0.25162791104446125,
            0.2560131584513188,
            0.2603984328219278,
            0.2647837080522762,
            0.2691690003160843,
            0.27355428538673887,
            0.27793956580603646,
            0.28232485772802646,
            0.2867101473502729,
            0.2910953976393595,
            0.2954806805365236,
            0.29986599000671765,
            0.30425125993844393,
            0.30863653737910707,
            0.31302181892322023,
            0.31740710595296057,
            0.32179238393160337,
            0.32617766091475214,
            0.33056297669645884,
            0.33494824661728656,
            0.3393335110414479,
            0.34371879447056264,
            0.348104096768005,
            0.3524893750548251,
            0.35687467179839094,
            0.36125992227526676,
            0.36564521209589235,
            0.3700305154675066,
            0.37441578286922633,
            0.3788010765307923,
            0.38318633483534714,
            0.3875716174906368,
            0.3919569002881606,
            0.39634218311138036,
            0.40072746768298995,
            0.40511274978101924,
            0.40949803805357393,
            0.41388331617529217,
            0.41826859757510965,
            0.4226538819775222,
            0.427039168238086,
            0.43142445092009857,
            0.43580973491566904,
            0.44019501537687733,
            0.4445802988278324,
            0.44896558270540027,
            0.45335086054337154,
            0.4577361417031189,
            0.46212143351522506,
            0.46650670713671444,
            0.47089198980463304,
            0.47527727257450414,
            0.47966256498083726,
            0.48404784761376424,
            0.4884331214469147,
            0.49281840436302654,
            0.49720368702245804,
            0.5015889694459748,
            0.5059742596303459,
            0.5103595368062622,
            0.5147448186951188,
            0.519130101416778,
            0.5235153838255434
        ]
    },
    "symbol_portfolios": [
        {
            "symbol": "AAPL",
            "annual_expected_return": 0.3514847637140689,
            "annual_standard_deviation": 0.3287517105290497,
            "beta": 1.1936077442725428,
            "annual_sharpe_ratio": 1.0691496118710244,
            "annual_sortino_ratio": 1.5123352545633497,
            "stats_descriptive": {
                "daily_mean_return": 0.0013947808083891622,
                "annual_mean_return": 0.3514847637140689,
                "daily_variance": 0.0004288797110149845,
                "annual_variance": 0.1080776871757761,
                "daily_standard_deviation": 0.020709411170165715,
                "annual_standard_deviation": 0.3287517105290497,
                "daily_semi_variance": 0.00021434645946924867,
                "annual_semi_variance": 0.05401530778625067,
                "daily_semi_deviation": 0.014640575790222482,
                "annual_semi_deviation": 0.23241193555032982,
                "mean_absolute_deviation": 0.014612164716720699
            },
            "stats_moments": {
                "skew": 0.05379905421365394,
                "kurtosis": 8.023316171059822,
                "first_lower_partial_moment": 0.007306082358360349,
                "fourth_central_moment": 1.4757911775235688e-06,
                "fourth_lower_partial_moment": 7.056451491602412e-07
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.031759479222826514,
                "conditional_var_at_95": 0.04618159776376259,
                "entropic_var_at_95": 0.07500050082856859,
                "drawdown_at_risk_at_95": 0.22557234378343938,
                "conditional_dar_at_95": 0.2573327810110585,
                "entropic_dar_at_95": 0.2762142903161993,
                "entropic_risk_measure_at_95": 2.994551690894659,
                "worst_realization": 0.12864725631179874,
                "average_drawdown": 0.07827559395108745,
                "max_drawdown": 0.33534546559987144,
                "ulcer_index": 0.10683817949220088,
                "gini_mean_difference": 0.021669349244881175
            },
            "stats_ratios": {
                "daily_sharpe_ratio": 0.06735009493647526,
                "annual_sharpe_ratio": 1.0691496118710244,
                "daily_sortino_ratio": 0.09526816625071867,
                "annual_sortino_ratio": 1.5123352545633497,
                "mean_absolute_deviation_ratio": 0.09545340032973448,
                "calmar_ratio": 0.0041592356285305825,
                "value_at_risk_ratio_at_95": 0.0439169924230587,
                "conditional_var_ratio_at_95": 0.030202090787850733,
                "entropic_var_ratio_at_95": 0.01859695326004908,
                "drawdown_at_risk_ratio_at_95": 0.00618329705226728,
                "conditional_dar_ratio_at_95": 0.005420144308506205,
                "entropic_dar_ratio_at_95": 0.005049633046836467,
                "entropic_risk_measure_ratio_at_95": 0.00046577282757555424,
                "worst_realization_ratio": 0.010841900934200037,
                "average_drawdown_ratio": 0.017818846692632284,
                "ulcer_index_ratio": 0.013055078390688792,
                "gini_mean_difference_ratio": 0.064366529544889
            }
        },
        {
            "symbol": "CSCO",
            "annual_expected_return": 0.0861090026130696,
            "annual_standard_deviation": 0.2880454583678956,
            "beta": 0.9187995153126283,
            "annual_sharpe_ratio": 0.29894240687207785,
            "annual_sortino_ratio": 0.40826547500026017,
            "stats_descriptive": {
                "daily_mean_return": 0.00034170239132170474,
                "annual_mean_return": 0.0861090026130696,
                "daily_variance": 0.0003292467701840121,
                "annual_variance": 0.08297018608637105,
                "daily_standard_deviation": 0.018145158312453825,
                "annual_standard_deviation": 0.2880454583678956,
                "daily_semi_variance": 0.00017652705110214392,
                "annual_semi_variance": 0.044484816877740266,
                "daily_semi_deviation": 0.013286348298239962,
                "annual_semi_deviation": 0.21091424057597505,
                "mean_absolute_deviation": 0.011815822031974555
            },
            "stats_moments": {
                "skew": -0.5347792622840455,
                "kurtosis": 15.092085407218471,
                "first_lower_partial_moment": 0.005907911015987276,
                "fourth_central_moment": 1.636033909667217e-06,
                "fourth_lower_partial_moment": 9.95975663772395e-07
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.02452621454936532,
                "conditional_var_at_95": 0.04377432237066117,
                "entropic_var_at_95": 0.08182108172166151,
                "drawdown_at_risk_at_95": 0.33447076833068357,
                "conditional_dar_at_95": 0.36660685339159227,
                "entropic_dar_at_95": 0.37962193245440645,
                "entropic_risk_measure_at_95": 2.995555627929083,
                "worst_realization": 0.13730368365136703,
                "average_drawdown": 0.1211627850256002,
                "max_drawdown": 0.42027054721925405,
                "ulcer_index": 0.1598423197540805,
                "gini_mean_difference": 0.017750421894583764
            },
            "stats_ratios": {
                "daily_sharpe_ratio": 0.018831601545585816,
                "annual_sharpe_ratio": 0.29894240687207785,
                "daily_sortino_ratio": 0.025718307517722527,
                "annual_sortino_ratio": 0.40826547500026017,
                "mean_absolute_deviation_ratio": 0.02891905365509322,
                "calmar_ratio": 0.0008130533856883373,
                "value_at_risk_ratio_at_95": 0.013932129258428393,
                "conditional_var_ratio_at_95": 0.007806000705809295,
                "entropic_var_ratio_at_95": 0.004176214541920944,
                "drawdown_at_risk_ratio_at_95": 0.001021621091215575,
                "conditional_dar_ratio_at_95": 0.0009320676582025439,
                "entropic_dar_ratio_at_95": 0.0009001123541847627,
                "entropic_risk_measure_ratio_at_95": 0.00011406978663184893,
                "worst_realization_ratio": 0.0024886615000755128,
                "average_drawdown_ratio": 0.002820192613181574,
                "ulcer_index_ratio": 0.002137746698417655,
                "gini_mean_difference_ratio": 0.019250381390989325
            }
        },
        {
            "symbol": "NFLX",
            "annual_expected_return": 0.2579487099278358,
            "annual_standard_deviation": 0.4776779013616111,
            "beta": 1.0183795798012412,
            "annual_sharpe_ratio": 0.5400055334202363,
            "annual_sortino_ratio": 0.7412255210287844,
            "stats_descriptive": {
                "daily_mean_return": 0.0010236059917771263,
                "annual_mean_return": 0.2579487099278358,
                "daily_variance": 0.0009054610216239406,
                "annual_variance": 0.22817617744923302,
                "daily_standard_deviation": 0.030090879376049158,
                "annual_standard_deviation": 0.4776779013616111,
                "daily_semi_variance": 0.0004805797327035534,
                "annual_semi_variance": 0.12110609264129546,
                "daily_semi_deviation": 0.021922128836031264,
                "annual_semi_deviation": 0.3480030066555395,
                "mean_absolute_deviation": 0.019837529542499645
            },
            "stats_moments": {
                "skew": -1.336054349808762,
                "kurtosis": 25.024138577279906,
                "first_lower_partial_moment": 0.009918764771249823,
                "fourth_central_moment": 2.0516281787808902e-05,
                "fourth_lower_partial_moment": 1.7538737452612462e-05
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.03902514828050141,
                "conditional_var_at_95": 0.0659602773779179,
                "entropic_var_at_95": 0.18998266312705944,
                "drawdown_at_risk_at_95": 1.0681812535763673,
                "conditional_dar_at_95": 1.1440790777775307,
                "entropic_dar_at_95": 1.1633667469332631,
                "entropic_risk_measure_at_95": 2.9951678376118562,
                "worst_realization": 0.3511660252265294,
                "average_drawdown": 0.2805968476203713,
                "max_drawdown": 1.2592917613131953,
                "ulcer_index": 0.4288909391252483,
                "gini_mean_difference": 0.029674394545660912
            },
            "stats_ratios": {
                "daily_sharpe_ratio": 0.03401715114354104,
                "annual_sharpe_ratio": 0.5400055334202363,
                "daily_sortino_ratio": 0.046692818906105736,
                "annual_sortino_ratio": 0.7412255210287844,
                "mean_absolute_deviation_ratio": 0.051599469056072086,
                "calmar_ratio": 0.0008128426018682956,
                "value_at_risk_ratio_at_95": 0.026229394041497146,
                "conditional_var_ratio_at_95": 0.015518521638597713,
                "entropic_var_ratio_at_95": 0.0053878915840470335,
                "drawdown_at_risk_ratio_at_95": 0.0009582699456201848,
                "conditional_dar_ratio_at_95": 0.0008946986372354317,
                "entropic_dar_ratio_at_95": 0.0008798652655969767,
                "entropic_risk_measure_ratio_at_95": 0.0003417524650616175,
                "worst_realization_ratio": 0.002914877631219651,
                "average_drawdown_ratio": 0.003647959698969949,
                "ulcer_index_ratio": 0.0023866346858827073,
                "gini_mean_difference_ratio": 0.03449458725104136
            }
        },
        {
            "symbol": "AMD",
            "annual_expected_return": 0.523515390545931,
            "annual_standard_deviation": 0.5266045534304432,
            "beta": 1.520446550585429,
            "annual_sharpe_ratio": 0.9941338090140152,
            "annual_sortino_ratio": 1.4411179147231348,
            "stats_descriptive": {
                "daily_mean_return": 0.002077442025975917,
                "annual_mean_return": 0.523515390545931,
                "daily_variance": 0.0011004458559272878,
                "annual_variance": 0.2773123556936765,
                "daily_standard_deviation": 0.033172968753599485,
                "annual_standard_deviation": 0.5266045534304432,
                "daily_semi_variance": 0.00052367197519042,
                "annual_semi_variance": 0.13196533774798586,
                "daily_semi_deviation": 0.022883880247685708,
                "annual_semi_deviation": 0.3632703370053573,
                "mean_absolute_deviation": 0.02435421766341545
            },
            "stats_moments": {
                "skew": 0.20265001277415304,
                "kurtosis": 5.23302810825666,
                "first_lower_partial_moment": 0.012177108831707726,
                "fourth_central_moment": 6.33709803977058e-06,
                "fourth_lower_partial_moment": 2.6787662947512513e-06
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.050899220731250416,
                "conditional_var_at_95": 0.07053464350257696,
                "entropic_var_at_95": 0.09581840397048567,
                "drawdown_at_risk_at_95": 0.6618618607377431,
                "conditional_dar_at_95": 0.7675846250889717,
                "entropic_dar_at_95": 0.8034985012953423,
                "entropic_risk_measure_at_95": 2.9942034193405647,
                "worst_realization": 0.14638954769626722,
                "average_drawdown": 0.21312410137889407,
                "max_drawdown": 0.8919219488269297,
                "ulcer_index": 0.3018244152775702,
                "gini_mean_difference": 0.03578807347364054
            },
            "stats_ratios": {
                "daily_sharpe_ratio": 0.06262454353743967,
                "annual_sharpe_ratio": 0.9941338090140152,
                "daily_sortino_ratio": 0.09078189553041437,
                "annual_sortino_ratio": 1.4411179147231348,
                "mean_absolute_deviation_ratio": 0.08530111928401708,
                "calmar_ratio": 0.0023291746869871324,
                "value_at_risk_ratio_at_95": 0.040814810052689804,
                "conditional_var_ratio_at_95": 0.029452789761388928,
                "entropic_var_ratio_at_95": 0.02168103349556749,
                "drawdown_at_risk_ratio_at_95": 0.0031387849175359642,
                "conditional_dar_ratio_at_95": 0.0027064664378017183,
                "entropic_dar_ratio_at_95": 0.002585495831823973,
                "entropic_risk_measure_ratio_at_95": 0.000693821272314707,
                "worst_realization_ratio": 0.014191190960479274,
                "average_drawdown_ratio": 0.009747569667320828,
                "ulcer_index_ratio": 0.006882948896183284,
                "gini_mean_difference_ratio": 0.05804844531533787
            }
        },
        {
            "symbol": "CVX",
            "annual_expected_return": 0.17571255847321654,
            "annual_standard_deviation": 0.376932730381948,
            "beta": 1.0326591800686096,
            "annual_sharpe_ratio": 0.4661642365075753,
            "annual_sortino_ratio": 0.6526738562743987,
            "stats_descriptive": {
                "daily_mean_return": 0.0006972720574333989,
                "annual_mean_return": 0.17571255847321654,
                "daily_variance": 0.0005638027112428187,
                "annual_variance": 0.14207828323319033,
                "daily_standard_deviation": 0.023744530133123685,
                "annual_standard_deviation": 0.376932730381948,
                "daily_semi_variance": 0.00028761572733830755,
                "annual_semi_variance": 0.0724791632892535,
                "daily_semi_deviation": 0.016959237227490733,
                "annual_semi_deviation": 0.2692195447757341,
                "mean_absolute_deviation": 0.015293996184002054
            },
            "stats_moments": {
                "skew": -0.24903538836259623,
                "kurtosis": 22.87649070753486,
                "first_lower_partial_moment": 0.007646998092001027,
                "fourth_central_moment": 7.271830104976145e-06,
                "fourth_lower_partial_moment": 3.954713588272054e-06
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.030848147588671493,
                "conditional_var_at_95": 0.05237548231472815,
                "entropic_var_at_95": 0.12383547815825487,
                "drawdown_at_risk_at_95": 0.279428685052976,
                "conditional_dar_at_95": 0.3733833075753401,
                "entropic_dar_at_95": 0.5054121288666451,
                "entropic_risk_measure_at_95": 2.9953174591050638,
                "worst_realization": 0.22124781229224955,
                "average_drawdown": 0.10177427717306817,
                "max_drawdown": 0.7154188176185421,
                "ulcer_index": 0.13855004374586374,
                "gini_mean_difference": 0.02290577335455845
            },
            "stats_ratios": {
                "daily_sharpe_ratio": 0.029365586664555746,
                "annual_sharpe_ratio": 0.4661642365075753,
                "daily_sortino_ratio": 0.04111458835560887,
                "annual_sortino_ratio": 0.6526738562743987,
                "mean_absolute_deviation_ratio": 0.045591227370827055,
                "calmar_ratio": 0.0009746347737321903,
                "value_at_risk_ratio_at_95": 0.022603368822362007,
                "conditional_var_ratio_at_95": 0.013312947711744964,
                "entropic_var_ratio_at_95": 0.005630632414907172,
                "drawdown_at_risk_ratio_at_95": 0.0024953488841033098,
                "conditional_dar_ratio_at_95": 0.0018674430358478348,
                "entropic_dar_ratio_at_95": 0.0013796108514391762,
                "entropic_risk_measure_ratio_at_95": 0.00023278736459598134,
                "worst_realization_ratio": 0.0031515432862782924,
                "average_drawdown_ratio": 0.006851161971385765,
                "ulcer_index_ratio": 0.005032636862333833,
                "gini_mean_difference_ratio": 0.030440886960694375
            }
        },
        {
            "symbol": "PFE",
            "annual_expected_return": 0.04071964206547551,
            "annual_standard_deviation": 0.2780356784552679,
            "beta": 0.5676914982782568,
            "annual_sharpe_ratio": 0.14645473664282527,
            "annual_sortino_ratio": 0.21512090645842552,
            "stats_descriptive": {
                "daily_mean_return": 0.0001615858812122044,
                "annual_mean_return": 0.04071964206547551,
                "daily_variance": 0.0003067612638654012,
                "annual_variance": 0.07730383849408111,
                "daily_standard_deviation": 0.017514601447518045,
                "annual_standard_deviation": 0.2780356784552679,
                "daily_semi_variance": 0.00014218118332732835,
                "annual_semi_variance": 0.03582965819848674,
                "daily_semi_deviation": 0.01192397514788287,
                "annual_semi_deviation": 0.18928723728367622,
                "mean_absolute_deviation": 0.012342599439633527
            },
            "stats_moments": {
                "skew": 0.3374919102671968,
                "kurtosis": 7.1877464498540995,
                "first_lower_partial_moment": 0.006171299719816763,
                "fourth_central_moment": 6.763847162878873e-07,
                "fourth_lower_partial_moment": 2.5733603550018086e-07
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.024005326855911724,
                "conditional_var_at_95": 0.03863347743314487,
                "entropic_var_at_95": 0.05396691174936433,
                "drawdown_at_risk_at_95": 0.5285907908941126,
                "conditional_dar_at_95": 0.5956084633299944,
                "entropic_dar_at_95": 0.6187953207911455,
                "entropic_risk_measure_at_95": 2.9957236389659765,
                "worst_realization": 0.0773463492356764,
                "average_drawdown": 0.1755720267540958,
                "max_drawdown": 0.7124760604087051,
                "ulcer_index": 0.23741719084985738,
                "gini_mean_difference": 0.01833646944358177
            },
            "stats_ratios": {
                "daily_sharpe_ratio": 0.009225781225818437,
                "annual_sharpe_ratio": 0.14645473664282527,
                "daily_sortino_ratio": 0.013551343340471013,
                "annual_sortino_ratio": 0.21512090645842552,
                "mean_absolute_deviation_ratio": 0.013091722047896432,
                "calmar_ratio": 0.00022679482187726026,
                "value_at_risk_ratio_at_95": 0.006731251033660102,
                "conditional_var_ratio_at_95": 0.004182535250465825,
                "entropic_var_ratio_at_95": 0.0029941657948234866,
                "drawdown_at_risk_ratio_at_95": 0.0003056918205837099,
                "conditional_dar_ratio_at_95": 0.0002712954754013937,
                "entropic_dar_ratio_at_95": 0.0002611297722898304,
                "entropic_risk_measure_ratio_at_95": 5.393884773295658e-05,
                "worst_realization_ratio": 0.0020891209838469283,
                "average_drawdown_ratio": 0.0009203395563606483,
                "ulcer_index_ratio": 0.0006805989095978787,
                "gini_mean_difference_ratio": 0.00881226790737317
            }
        },
        {
            "symbol": "MMM",
            "annual_expected_return": -0.0061119533560863555,
            "annual_standard_deviation": 0.28153493709505667,
            "beta": 0.7904373651905431,
            "annual_sharpe_ratio": -0.02170939571177531,
            "annual_sortino_ratio": -0.030593938794936038,
            "stats_descriptive": {
                "daily_mean_return": -2.425378315907284e-05,
                "annual_mean_return": -0.0061119533560863555,
                "daily_variance": 0.0003145314317663393,
                "annual_variance": 0.07926192080511751,
                "daily_standard_deviation": 0.017735034022136505,
                "annual_standard_deviation": 0.28153493709505667,
                "daily_semi_variance": 0.0001583757682692267,
                "annual_semi_variance": 0.03991069360384513,
                "daily_semi_deviation": 0.012584743472523653,
                "annual_semi_deviation": 0.19977660925104604,
                "mean_absolute_deviation": 0.012240243364360904
            },
            "stats_moments": {
                "skew": 0.03534315584460515,
                "kurtosis": 9.164868524830545,
                "first_lower_partial_moment": 0.006120121682180452,
                "fourth_central_moment": 9.066806408383826e-07,
                "fourth_lower_partial_moment": 4.159786915828121e-07
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.025948118449920177,
                "conditional_var_at_95": 0.04175418720045489,
                "entropic_var_at_95": 0.06350243717714531,
                "drawdown_at_risk_at_95": 0.589375544638203,
                "conditional_dar_at_95": 0.6327045520817631,
                "entropic_dar_at_95": 0.6520386460687586,
                "entropic_risk_measure_at_95": 2.9959136384063787,
                "worst_realization": 0.09540479602794527,
                "average_drawdown": 0.24125521674055359,
                "max_drawdown": 0.7014185230057153,
                "ulcer_index": 0.32276335340716333,
                "gini_mean_difference": 0.01827949065613451
            },
            "stats_ratios": {
                "daily_sharpe_ratio": -0.001367563384924989,
                "annual_sharpe_ratio": -0.02170939571177531,
                "daily_sortino_ratio": -0.0019272369923174256,
                "annual_sortino_ratio": -0.030593938794936038,
                "mean_absolute_deviation_ratio": -0.0019814788347828896,
                "calmar_ratio": -3.457819028665032e-05,
                "value_at_risk_ratio_at_95": -0.0009347029614452624,
                "conditional_var_ratio_at_95": -0.0005808706811279662,
                "entropic_var_ratio_at_95": -0.0003819346821510945,
                "drawdown_at_risk_ratio_at_95": -4.115166192374234e-05,
                "conditional_dar_ratio_at_95": -3.833350507637658e-05,
                "entropic_dar_ratio_at_95": -3.7196849151967655e-05,
                "entropic_risk_measure_ratio_at_95": -8.095621598750155e-06,
                "worst_realization_ratio": -0.0002542197475268287,
                "average_drawdown_ratio": -0.00010053164232778192,
                "ulcer_index_ratio": -7.51441664707111e-05,
                "gini_mean_difference_ratio": -0.0013268303595173417
            }
        },
        {
            "symbol": "MSFT",
            "annual_expected_return": 0.2981343195184938,
            "annual_standard_deviation": 0.3181090994980832,
            "beta": 1.174859610824619,
            "annual_sharpe_ratio": 0.9372077692492736,
            "annual_sortino_ratio": 1.32636126221595,
            "stats_descriptive": {
                "daily_mean_return": 0.0011830726965019595,
                "annual_mean_return": 0.2981343195184938,
                "daily_variance": 0.0004015611078709579,
                "annual_variance": 0.1011933991834814,
                "daily_standard_deviation": 0.02003898969187214,
                "annual_standard_deviation": 0.3181090994980832,
                "daily_semi_variance": 0.00020049324514731233,
                "annual_semi_variance": 0.05052429777712271,
                "daily_semi_deviation": 0.014159563734356801,
                "annual_semi_deviation": 0.22477610588566282,
                "mean_absolute_deviation": 0.014032933311108577
            },
            "stats_moments": {
                "skew": 0.013094708142127345,
                "kurtosis": 9.81992330927755,
                "first_lower_partial_moment": 0.0070164666555542895,
                "fourth_central_moment": 1.5834756288612073e-06,
                "fourth_lower_partial_moment": 8.052237155742916e-07
            },
            "stats_risk_measures": {
                "value_at_risk_at_95": 0.029281858436955632,
                "conditional_var_at_95": 0.044462130063722044,
                "entropic_var_at_95": 0.0825777383462029,
                "drawdown_at_risk_at_95": 0.28591384609781156,
                "conditional_dar_at_95": 0.3231588290994126,
                "entropic_dar_at_95": 0.34397949744378653,
                "entropic_risk_measure_at_95": 2.9947498219993287,
                "worst_realization": 0.14739016963703078,
                "average_drawdown": 0.08936083792001571,
                "max_drawdown": 0.4101254092203992,
                "ulcer_index": 0.13191539155332965,
                "gini_mean_difference": 0.02083317520022314
            },
            "stats_ratios": {
                "daily_sharpe_ratio": 0.059038540100742526,
                "annual_sharpe_ratio": 0.9372077692492736,
                "daily_sortino_ratio": 0.08355290591555084,
                "annual_sortino_ratio": 1.32636126221595,
                "mean_absolute_deviation_ratio": 0.08430687086394333,
                "calmar_ratio": 0.0028846608132640293,
                "value_at_risk_ratio_at_95": 0.04040292384614645,
                "conditional_var_ratio_at_95": 0.026608547426909337,
                "entropic_var_ratio_at_95": 0.014326775232593418,
                "drawdown_at_risk_ratio_at_95": 0.004137864299503804,
                "conditional_dar_ratio_at_95": 0.0036609635571430215,
                "entropic_dar_ratio_at_95": 0.003439369803414805,
                "entropic_risk_measure_ratio_at_95": 0.00039504892455828806,
                "worst_realization_ratio": 0.008026808703833125,
                "average_drawdown_ratio": 0.013239274877445681,
                "ulcer_index_ratio": 0.008968420459288685,
                "gini_mean_difference_ratio": 0.05678792047451739
            }
        }
    ],
    "strategy_results": [
        {
            "name": "Min Variance",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.0920011387554353,
                    "annual_standard_deviation": 0.2139985900848926,
                    "annual_sharpe_ratio": 0.4299146957881298,
                    "annual_sortino_ratio": 0.6010427440480168,
                    "cvar_900": -0.023553997748657327,
                    "cvar_950": -0.030652136494590553,
                    "cvar_990": -0.05523835794146369,
                    "cvar_999": -0.09611300997315249,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.12102832390401454
                        }
                    ]
                },
                "weights": [
                    0.03395705478778786,
                    0.13936984015593576,
                    0.0752419517315904,
                    1.296097742646796e-08,
                    0.07111097550852417,
                    0.3439935744872134,
                    0.2567548414167036,
                    0.07957174895126715
                ],
                "position": [
                    0.2139985900848926,
                    0.0920011387554353
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.00036508388395014007,
                        "annual_mean_return": 0.0920011387554353,
                        "daily_variance": 0.000181727764120325,
                        "annual_variance": 0.0457953965583219,
                        "daily_standard_deviation": 0.013480644054359012,
                        "annual_standard_deviation": 0.2139985900848926,
                        "daily_semi_variance": 9.297691837658334e-05,
                        "annual_semi_variance": 0.023430183430899004,
                        "daily_semi_deviation": 0.009642453960304054,
                        "annual_semi_deviation": 0.15306921124412642,
                        "mean_absolute_deviation": 0.009204117404608988
                    },
                    "stats_moments": {
                        "skew": -0.10040647902475203,
                        "kurtosis": 12.35946204597939,
                        "first_lower_partial_moment": 0.004602058702304494,
                        "fourth_central_moment": 4.0817098999594454e-07,
                        "fourth_lower_partial_moment": 2.1407079804972848e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.01910946194250858,
                        "conditional_var_at_95": 0.030652136494590553,
                        "entropic_var_at_95": 0.05714918946216186,
                        "drawdown_at_risk_at_95": 0.2764572088895355,
                        "conditional_dar_at_95": 0.29610268089937186,
                        "entropic_dar_at_95": 0.30870343803926037,
                        "entropic_risk_measure_at_95": 2.9954580224508702,
                        "worst_realization": 0.0968490771343743,
                        "average_drawdown": 0.11372823857905126,
                        "max_drawdown": 0.3394216213424398,
                        "ulcer_index": 0.15315017685511173,
                        "gini_mean_difference": 0.013634523444941014
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.02708208023874712,
                        "annual_sharpe_ratio": 0.4299146957881298,
                        "daily_sortino_ratio": 0.037862134001688086,
                        "annual_sortino_ratio": 0.6010427440480168,
                        "mean_absolute_deviation_ratio": 0.039665278907385866,
                        "calmar_ratio": 0.0010756058571230788,
                        "value_at_risk_ratio_at_95": 0.019104875116238568,
                        "conditional_var_ratio_at_95": 0.011910552597681718,
                        "entropic_var_ratio_at_95": 0.006388260050334746,
                        "drawdown_at_risk_ratio_at_95": 0.001320580083321384,
                        "conditional_dar_ratio_at_95": 0.0012329637909432199,
                        "entropic_dar_ratio_at_95": 0.0011826362747009943,
                        "entropic_risk_measure_ratio_at_95": 0.00012187915210757322,
                        "worst_realization_ratio": 0.0037696165492996955,
                        "average_drawdown_ratio": 0.0032101427799426808,
                        "ulcer_index_ratio": 0.002383829333057375,
                        "gini_mean_difference_ratio": 0.02677643156538791
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 1.2397173610112784e-05,
                            "CSCO": 5.088168320911559e-05,
                            "NFLX": 2.746962433019118e-05,
                            "CVX": 2.5961471466621346e-05,
                            "PFE": 0.00012558651185540768,
                            "MMM": 9.373705594233634e-05,
                            "MSFT": 2.905036353635521e-05
                        },
                        "annual_mean_return": {
                            "AAPL": 0.0031240877497484216,
                            "CSCO": 0.012822184168697126,
                            "NFLX": 0.006922345331208177,
                            "CVX": 0.006542290809588579,
                            "PFE": 0.03164780098756273,
                            "MMM": 0.023621738097468755,
                            "MSFT": 0.007320691611161512
                        },
                        "daily_variance": {
                            "AAPL": 6.170939722677478e-06,
                            "CSCO": 2.532736976561277e-05,
                            "NFLX": 1.367355183345394e-05,
                            "CVX": 1.2922838751071915e-05,
                            "PFE": 6.251318397355175e-05,
                            "MMM": 4.66594838624787e-05,
                            "MSFT": 1.4460396211478467e-05
                        },
                        "annual_variance": {
                            "AAPL": 0.0015550768101147243,
                            "CSCO": 0.006382497180934417,
                            "NFLX": 0.0034457350620303927,
                            "CVX": 0.0032565553652701223,
                            "PFE": 0.015753322361335042,
                            "MMM": 0.011758189933344631,
                            "MSFT": 0.0036440198452925734
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.0004577629746615914,
                            "CSCO": 0.0018787952314061043,
                            "NFLX": 0.001014309982395281,
                            "CVX": 0.0009586217616133311,
                            "PFE": 0.004637254994752116,
                            "MMM": 0.003461220671232781,
                            "MSFT": 0.0010726784382978087
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.0072667619422063946,
                            "CSCO": 0.02982494968028761,
                            "NFLX": 0.0161016717944893,
                            "CVX": 0.015217648695621108,
                            "PFE": 0.0736141408926374,
                            "MMM": 0.05494517477278795,
                            "MSFT": 0.01702824230686287
                        },
                        "daily_semi_variance": {
                            "AAPL": 3.1572223522340096e-06,
                            "CSCO": 1.2958178420286568e-05,
                            "NFLX": 6.995764895314858e-06,
                            "CVX": 6.611679451229099e-06,
                            "PFE": 3.1983462911703736e-05,
                            "MMM": 2.387227424260147e-05,
                            "MSFT": 7.398336103213616e-06
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.0007956200327629704,
                            "CSCO": 0.0032654609619122157,
                            "NFLX": 0.0017629327536193443,
                            "CVX": 0.0016661432217097332,
                            "PFE": 0.008059832653749342,
                            "MMM": 0.0060158131091355704,
                            "MSFT": 0.0018643806980098313
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.00032742934166257124,
                            "CSCO": 0.0013438672845763797,
                            "NFLX": 0.0007255170648586909,
                            "CVX": 0.0006856843163003927,
                            "PFE": 0.003316942247624193,
                            "MMM": 0.002475746769533832,
                            "MSFT": 0.0007672669357479954
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.005197779659908581,
                            "CSCO": 0.021333231780388606,
                            "NFLX": 0.01151722635329769,
                            "CVX": 0.010884901072969149,
                            "PFE": 0.05265482580226343,
                            "MMM": 0.039301261568148366,
                            "MSFT": 0.01217998500715062
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.00031254472303242445,
                            "CSCO": 0.001282776388082857,
                            "NFLX": 0.0006925357664654213,
                            "CVX": 0.0006545137758198693,
                            "PFE": 0.0031661572870479134,
                            "MMM": 0.0023632017352305077,
                            "MSFT": 0.0007323877289299959
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.0034095083534829394,
                            "CSCO": -0.0139936351136712,
                            "NFLX": -0.0075547795462366655,
                            "CVX": -0.0071400027633677044,
                            "PFE": -0.034539184069061465,
                            "MMM": -0.025779849933341845,
                            "MSFT": -0.007989519245590219
                        },
                        "kurtosis": {
                            "AAPL": 0.41969093528251167,
                            "CSCO": 1.7225362720872566,
                            "NFLX": 0.9299500587450668,
                            "CVX": 0.8788934142414925,
                            "PFE": 4.251575583040075,
                            "MMM": 3.1733517587409468,
                            "MSFT": 0.9834640238420419
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.00015627236151621223,
                            "CSCO": 0.0006413881940414285,
                            "NFLX": 0.00034626788323271064,
                            "CVX": 0.00032725688790993465,
                            "PFE": 0.0015830786435239567,
                            "MMM": 0.0011816008676152538,
                            "MSFT": 0.00036619386446499797
                        },
                        "fourth_central_moment": {
                            "AAPL": 1.3860284849720744e-08,
                            "CSCO": 5.6886726369332435e-08,
                            "NFLX": 3.071158232556246e-08,
                            "CVX": 2.902543764908973e-08,
                            "PFE": 1.4040819967051713e-07,
                            "MMM": 1.0479987916561656e-07,
                            "MSFT": 3.247887996610551e-08
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 7.269213912056221e-09,
                            "CSCO": 2.9835013292935204e-08,
                            "NFLX": 1.6107104862764533e-08,
                            "CVX": 1.5222783474506623e-08,
                            "PFE": 7.363897996888968e-08,
                            "MMM": 5.4963714517588704e-08,
                            "MSFT": 1.7033988020987542e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.000648901054557303,
                            "CSCO": 0.002663282690912106,
                            "NFLX": 0.0014378332317306188,
                            "CVX": 0.0013588924977873777,
                            "PFE": 0.0065735322053303,
                            "MMM": 0.0049064469341996726,
                            "MSFT": 0.0015205733279912035
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.0010408562918000784,
                            "CSCO": 0.004271983419058092,
                            "NFLX": 0.002306326604488351,
                            "CVX": 0.0021797033558018557,
                            "PFE": 0.010544138135106507,
                            "MMM": 0.00787008454675574,
                            "MSFT": 0.00243904414157993
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.0019406181827966082,
                            "CSCO": 0.007964873503615334,
                            "NFLX": 0.004300016610743917,
                            "CVX": 0.004063934664848366,
                            "PFE": 0.019658954216935316,
                            "MMM": 0.014673331267631238,
                            "MSFT": 0.004547461015591087
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.009387672710414288,
                            "CSCO": 0.038529797512274554,
                            "NFLX": 0.02080118023672027,
                            "CVX": 0.019659142065300415,
                            "PFE": 0.09509950471125211,
                            "MMM": 0.07098172774692979,
                            "MSFT": 0.02199818390664411
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.010054775088430553,
                            "CSCO": 0.04126778384156034,
                            "NFLX": 0.022279343912587134,
                            "CVX": 0.021056150762351882,
                            "PFE": 0.10185742093799342,
                            "MMM": 0.07602579786274768,
                            "MSFT": 0.023561408493700874
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.01048265969454316,
                            "CSCO": 0.04302394937275199,
                            "NFLX": 0.023227449485376493,
                            "CVX": 0.021952202906329068,
                            "PFE": 0.10619200048396933,
                            "MMM": 0.07926110330586289,
                            "MSFT": 0.02456407279042748
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 0.1017169335012338,
                            "CSCO": 0.41747651119369694,
                            "NFLX": 0.22538411086045207,
                            "CVX": 0.21300994483213326,
                            "PFE": 1.0304183257245034,
                            "MMM": 0.7690983594930325,
                            "MSFT": 0.23835383684581854
                        },
                        "worst_realization": {
                            "AAPL": 0.003288709461023531,
                            "CSCO": 0.01349784057441285,
                            "NFLX": 0.0072871136814417845,
                            "CVX": 0.006887032441388333,
                            "PFE": 0.033315460661042205,
                            "MMM": 0.02486646976328413,
                            "MSFT": 0.007706450551781472
                        },
                        "average_drawdown": {
                            "AAPL": 0.003861876078401143,
                            "CSCO": 0.015850286637413714,
                            "NFLX": 0.008557134748592606,
                            "CVX": 0.008087326093042161,
                            "PFE": 0.03912178381599902,
                            "MMM": 0.02920027623942947,
                            "MSFT": 0.009049554966173162
                        },
                        "max_drawdown": {
                            "AAPL": 0.011525758741470117,
                            "CSCO": 0.047305137725085225,
                            "NFLX": 0.02553874558071312,
                            "CVX": 0.024136602915179776,
                            "PFE": 0.11675885829714028,
                            "MMM": 0.08714814569070373,
                            "MSFT": 0.02700837239214759
                        },
                        "ulcer_index": {
                            "AAPL": 0.005200529013632371,
                            "CSCO": 0.02134451594479601,
                            "NFLX": 0.011523318363970324,
                            "CVX": 0.01089065861662358,
                            "PFE": 0.052682677452557794,
                            "MMM": 0.03932204988102654,
                            "MSFT": 0.01218642758250513
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.00046298826562602075,
                            "CSCO": 0.0019002413777527737,
                            "NFLX": 0.001025888168224003,
                            "CVX": 0.0009695642753301001,
                            "PFE": 0.0046901885170444035,
                            "MMM": 0.0035007299502710404,
                            "MSFT": 0.0010849228906926738
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.0009196276943536771,
                            "CSCO": 0.0037744252428846543,
                            "NFLX": 0.002037708600525565,
                            "CVX": 0.0019258331695381139,
                            "PFE": 0.009316061706621416,
                            "MMM": 0.006953455307057539,
                            "MSFT": 0.002154968517766158
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.014598637068165285,
                            "CSCO": 0.059917143209264154,
                            "NFLX": 0.03234762120844863,
                            "CVX": 0.030571653799182842,
                            "PFE": 0.14788789484551343,
                            "MMM": 0.11038268097045911,
                            "MSFT": 0.03420906468709638
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.0012856865753416431,
                            "CSCO": 0.00527683963217089,
                            "NFLX": 0.0028488208959335268,
                            "CVX": 0.002692413318590811,
                            "PFE": 0.013024330981762611,
                            "MMM": 0.009721286337298782,
                            "MSFT": 0.0030127562605898267
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 0.020409641653969777,
                            "CSCO": 0.08376723225056235,
                            "NFLX": 0.04522362972242598,
                            "CVX": 0.042740736405536425,
                            "PFE": 0.20675484462442556,
                            "MMM": 0.1543206364328553,
                            "MSFT": 0.04782602295824153
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.0013469160664883373,
                            "CSCO": 0.005528143652713125,
                            "NFLX": 0.002984493039651546,
                            "CVX": 0.0028206367134801067,
                            "PFE": 0.013644601251231308,
                            "MMM": 0.010184252527613047,
                            "MSFT": 0.0031562356562084
                        },
                        "calmar_ratio": {
                            "AAPL": 3.6524407493785945e-05,
                            "CSCO": 0.00014990701832097328,
                            "NFLX": 8.093068503281143e-05,
                            "CVX": 7.648738275405568e-05,
                            "PFE": 0.0003700015083267321,
                            "MMM": 0.0002761670148519082,
                            "MSFT": 8.558784034281223e-05
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.0006487452994443315,
                            "CSCO": 0.002662643425659746,
                            "NFLX": 0.0014374881099653363,
                            "CVX": 0.0013585663240926016,
                            "PFE": 0.006571954366545676,
                            "MMM": 0.004905269244332846,
                            "MSFT": 0.0015202083461980326
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.0004044472923543395,
                            "CSCO": 0.0016599718332226245,
                            "NFLX": 0.0008961732352666178,
                            "CVX": 0.0008469710250443062,
                            "PFE": 0.004097153615297616,
                            "MMM": 0.0030580920830389404,
                            "MSFT": 0.000947743513457275
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.00021692649933943294,
                            "CSCO": 0.0008903307936292612,
                            "NFLX": 0.00048066516058602464,
                            "CVX": 0.000454275409869291,
                            "PFE": 0.0021975204379505284,
                            "MMM": 0.0016402167174111731,
                            "MSFT": 0.000508325031549035
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 4.484301082221497e-05,
                            "CSCO": 0.0001840490375110691,
                            "NFLX": 9.936302417480916e-05,
                            "CVX": 9.390773917924787e-05,
                            "PFE": 0.0004542710691461423,
                            "MMM": 0.0003390653342658575,
                            "MSFT": 0.00010508086822204342
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 4.1867819543065414e-05,
                            "CSCO": 0.00017183796868900123,
                            "NFLX": 9.27706032473462e-05,
                            "CVX": 8.767725907704344e-05,
                            "PFE": 0.00042413162715702413,
                            "MMM": 0.0003165694267192134,
                            "MSFT": 9.81090865105262e-05
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 4.01588452945449e-05,
                            "CSCO": 0.0001648238307039669,
                            "NFLX": 8.898386265039796e-05,
                            "CVX": 8.409842025575243e-05,
                            "PFE": 0.0004068192847254128,
                            "MMM": 0.0003036475931000646,
                            "MSFT": 9.410443797085485e-05
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 4.138657099247037e-06,
                            "CSCO": 1.6986278167732232e-05,
                            "NFLX": 9.170425398822867e-06,
                            "CVX": 8.66694551285342e-06,
                            "PFE": 4.192564573235226e-05,
                            "MMM": 3.129306277697095e-05,
                            "MSFT": 9.698137419594461e-06
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.00012800507735259256,
                            "CSCO": 0.0005253708627343888,
                            "NFLX": 0.0002836333101251771,
                            "CVX": 0.00026806111358811216,
                            "PFE": 0.0012967238880465667,
                            "MMM": 0.0009678673118617315,
                            "MSFT": 0.0002999549855911272
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.0001090069956679725,
                            "CSCO": 0.00044739709191704644,
                            "NFLX": 0.00024153741123052162,
                            "CVX": 0.00022827638756205487,
                            "PFE": 0.0011042685037992025,
                            "MMM": 0.0008242197110718524,
                            "MSFT": 0.0002554366786940309
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 8.094782431652804e-05,
                            "CSCO": 0.0003322339174133137,
                            "NFLX": 0.00017936397393898484,
                            "CVX": 0.00016951643151664323,
                            "PFE": 0.0008200219838741631,
                            "MMM": 0.0006120597303065253,
                            "MSFT": 0.0001896854716912172
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.0009092487654720826,
                            "CSCO": 0.003731827035582593,
                            "NFLX": 0.002014710997499775,
                            "CVX": 0.0019040981939309476,
                            "PFE": 0.009210920525572574,
                            "MMM": 0.006874978529382834,
                            "MSFT": 0.002130647517947107
                        }
                    }
                },
                "allocation": {
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.3439935744872134,
                        "Shares": 12090,
                        "Purchase Value": 343991.363296386,
                        "Current Value": 345532.19907753303,
                        "Net Value": 1540.8357811470632,
                        "Net Change": 0.004479286242484715,
                        "%Shares": 0.6409033078880407,
                        "%Purchase Value": 0.34399481366372886,
                        "%Current Value": 0.2866621395238297
                    },
                    "MMM": {
                        "Company Name": "3M Company",
                        "Sector": "Industrials",
                        "Industry": "Conglomerates",
                        "Market Cap": 74311114752,
                        "Volume (3 Months Average)": 4169252.3076923075,
                        "Current Price": 135.2700042725,
                        "Purchase Price": 89.3647994995,
                        "Price Diff": 45.905204772999994,
                        "Weight": 0.2567548414167036,
                        "Shares": 2873,
                        "Purchase Value": 256745.0689620635,
                        "Current Value": 388630.72227489244,
                        "Net Value": 131885.65331282894,
                        "Net Change": 0.5136832962206425,
                        "%Shares": 0.15230067854113655,
                        "%Purchase Value": 0.2567476442150957,
                        "%Current Value": 0.3224177504424527
                    },
                    "CSCO": {
                        "Company Name": "Cisco Systems, Inc.",
                        "Sector": "Technology",
                        "Industry": "Communication Equipment",
                        "Market Cap": 210511003648,
                        "Volume (3 Months Average)": 18805300.0,
                        "Current Price": 52.75,
                        "Purchase Price": 48.9177017212,
                        "Price Diff": 3.8322982788000033,
                        "Weight": 0.13936984015593576,
                        "Shares": 2849,
                        "Purchase Value": 139366.5322036988,
                        "Current Value": 150284.75,
                        "Net Value": 10918.217796301207,
                        "Net Change": 0.0783417483642564,
                        "%Shares": 0.1510284139100933,
                        "%Purchase Value": 0.13936793010429374,
                        "%Current Value": 0.12467998087534832
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.07957174895126715,
                        "Shares": 216,
                        "Purchase Value": 79672.484619144,
                        "Current Value": 89868.9594726576,
                        "Net Value": 10196.474853513602,
                        "Net Change": 0.12797987789957233,
                        "%Shares": 0.011450381679389313,
                        "%Purchase Value": 0.07967328376519354,
                        "%Current Value": 0.07455753260619193
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.0752419517315904,
                        "Shares": 160,
                        "Purchase Value": 74960.0,
                        "Current Value": 115152.00195312,
                        "Net Value": 40192.001953119994,
                        "Net Change": 0.5361793216798292,
                        "%Shares": 0.008481764206955046,
                        "%Purchase Value": 0.07496075187799352,
                        "%Current Value": 0.09553297590921948
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.07111097550852417,
                        "Shares": 492,
                        "Purchase Value": 71225.8886718504,
                        "Current Value": 74164.0827026544,
                        "Net Value": 2938.194030803992,
                        "Net Change": 0.0412517707478631,
                        "%Shares": 0.02608142493638677,
                        "%Purchase Value": 0.07122660309525304,
                        "%Current Value": 0.06152837472201738
                    },
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.03395705478778786,
                        "Shares": 184,
                        "Purchase Value": 34028.6319580104,
                        "Current Value": 41731.2005615312,
                        "Net Value": 7702.568603520798,
                        "Net Change": 0.22635551770125156,
                        "%Shares": 0.009754028837998304,
                        "%Purchase Value": 0.03402897327844155,
                        "%Current Value": 0.03462124592094031
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 10.030288846950782
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.0920011387554353,
                    "Expected Daily Return": 0.00036508388395014007,
                    "Expected Current Return": 0.06973102183447676,
                    "Net Value": 205373.9463312358,
                    "Net Change": 0.20537600631190134,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.023553997748657327,
                        "95.0% CVaR": 0.030652136494590553,
                        "99.0% CVaR": 0.05523835794146369,
                        "99.9% CVaR": 0.09611300997315249
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.047437936947065745,
                        "95.0% EVaR": 0.05714918946216186,
                        "99.0% EVaR": 0.0770109008339637,
                        "99.9% EVaR": 0.09670779963385387
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.28245346309747627,
                        "95.0% CDaR": 0.29610268089937186,
                        "99.0% CDaR": 0.3221404970485751,
                        "99.9% CDaR": 0.3392565532082848
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.2954301027740148,
                        "95.0% EDaR": 0.30870343803926037,
                        "99.0% EDaR": 0.32912190573480066,
                        "99.9% EDaR": 0.3410383291801953
                    },
                    "VaR": {
                        "90.0% VaR": 0.014099491571908485,
                        "95.0% VaR": 0.01910946194250858,
                        "99.0% VaR": 0.03430093184626235,
                        "99.9% VaR": 0.0854453699554451
                    },
                    "DaR": {
                        "90.0% DaR": 0.2622254873161645,
                        "95.0% DaR": 0.2764572088895355,
                        "99.0% DaR": 0.30898966382947224,
                        "99.9% DaR": 0.33686426140893627
                    },
                    "ERM": {
                        "90.0% ERM": 2.302310841890926,
                        "95.0% ERM": 2.9954580224508702,
                        "99.0% ERM": 4.604895934884971,
                        "99.9% ERM": 6.907481027879016
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.0007998244023890951,
                            "CSCO": 0.0032827169438108634,
                            "NFLX": 0.0017722487846605407,
                            "CVX": 0.0016749477787415656,
                            "PFE": 0.008102423984039748,
                            "MMM": 0.006047603035068755,
                            "MSFT": 0.0018742328199467622
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.0010408562918000784,
                            "CSCO": 0.004271983419058092,
                            "NFLX": 0.002306326604488351,
                            "CVX": 0.0021797033558018557,
                            "PFE": 0.010544138135106507,
                            "MMM": 0.00787008454675574,
                            "MSFT": 0.00243904414157993
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.0018757319713170397,
                            "CSCO": 0.007698561216559039,
                            "NFLX": 0.004156241915832883,
                            "CVX": 0.003928053569617931,
                            "PFE": 0.019001640443368085,
                            "MMM": 0.014182716017201486,
                            "MSFT": 0.00439541280756723
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.0032637147877784753,
                            "CSCO": 0.013395255010479723,
                            "NFLX": 0.007231730550908105,
                            "CVX": 0.006834689986835651,
                            "PFE": 0.03306225828390911,
                            "MMM": 0.024677480953583103,
                            "MSFT": 0.007647880399658333
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.0016108526448093629,
                            "CSCO": 0.006611417775330351,
                            "NFLX": 0.003569323008279266,
                            "CVX": 0.0033733580161397245,
                            "PFE": 0.01631834570822191,
                            "MMM": 0.012179920135843125,
                            "MSFT": 0.003774719658442013
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.0019406181827966082,
                            "CSCO": 0.007964873503615334,
                            "NFLX": 0.004300016610743917,
                            "CVX": 0.004063934664848366,
                            "PFE": 0.019658954216935316,
                            "MMM": 0.014673331267631238,
                            "MSFT": 0.004547461015591087
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.002615063412769582,
                            "CSCO": 0.010732997078604277,
                            "NFLX": 0.005794450558457136,
                            "CVX": 0.005476320354071843,
                            "PFE": 0.02649125539570807,
                            "MMM": 0.019772921887258238,
                            "MSFT": 0.0061278921470945625
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.0032839120931358987,
                            "CSCO": 0.013478150751492488,
                            "NFLX": 0.007276483686429092,
                            "CVX": 0.006876986060378709,
                            "PFE": 0.03326686210801368,
                            "MMM": 0.024830196080572117,
                            "MSFT": 0.007695208853831895
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.009591287845713888,
                            "CSCO": 0.039365494513601065,
                            "NFLX": 0.021252350112252096,
                            "CVX": 0.020085541556950727,
                            "PFE": 0.0971621776565099,
                            "MMM": 0.07252129506513816,
                            "MSFT": 0.022475316347310453
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.010054775088430553,
                            "CSCO": 0.04126778384156034,
                            "NFLX": 0.022279343912587134,
                            "CVX": 0.021056150762351882,
                            "PFE": 0.10185742093799342,
                            "MMM": 0.07602579786274768,
                            "MSFT": 0.023561408493700874
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.010938942649423073,
                            "CSCO": 0.04489667016331835,
                            "NFLX": 0.024238480043873828,
                            "CVX": 0.022907725292831548,
                            "PFE": 0.11081426250308817,
                            "MMM": 0.08271113330562214,
                            "MSFT": 0.025633283090418044
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.011520153513722249,
                            "CSCO": 0.047282132205315026,
                            "NFLX": 0.02552632553196963,
                            "CVX": 0.024124864758982505,
                            "PFE": 0.1167020759189024,
                            "MMM": 0.0871057636475465,
                            "MSFT": 0.026995237631846514
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.010031936315882724,
                            "CSCO": 0.04117404673452202,
                            "NFLX": 0.02222873782108739,
                            "CVX": 0.021008323075132156,
                            "PFE": 0.10162605838153127,
                            "MMM": 0.0758531101705931,
                            "MSFT": 0.023507890275266202
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.01048265969454316,
                            "CSCO": 0.04302394937275199,
                            "NFLX": 0.023227449485376493,
                            "CVX": 0.021952202906329068,
                            "PFE": 0.10619200048396933,
                            "MMM": 0.07926110330586289,
                            "MSFT": 0.02456407279042748
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.011176010729749804,
                            "CSCO": 0.04586966798859187,
                            "NFLX": 0.024763774866069652,
                            "CVX": 0.023404180081367267,
                            "PFE": 0.11321582226314554,
                            "MMM": 0.08450364380895187,
                            "MSFT": 0.026188805996924698
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.011580657378804166,
                            "CSCO": 0.04753045804093242,
                            "NFLX": 0.025660389835382234,
                            "CVX": 0.02425156858812491,
                            "PFE": 0.11731499541235936,
                            "MMM": 0.08756324326058385,
                            "MSFT": 0.02713701666400837
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.0004787772139926704,
                            "CSCO": 0.001965043912125739,
                            "NFLX": 0.0010608732780434589,
                            "CVX": 0.0010026286128476745,
                            "PFE": 0.004850134567135625,
                            "MMM": 0.0036201127695217133,
                            "MSFT": 0.0011219212182416048
                        },
                        "95.0% VaR": {
                            "AAPL": 0.000648901054557303,
                            "CSCO": 0.002663282690912106,
                            "NFLX": 0.0014378332317306188,
                            "CVX": 0.0013588924977873777,
                            "PFE": 0.0065735322053303,
                            "MMM": 0.0049064469341996726,
                            "MSFT": 0.0015205733279912035
                        },
                        "99.0% VaR": {
                            "AAPL": 0.001164758637072119,
                            "CSCO": 0.004780515450573385,
                            "NFLX": 0.002580869091775631,
                            "CVX": 0.0024391727560531826,
                            "PFE": 0.011799300306968548,
                            "MMM": 0.008806930430778678,
                            "MSFT": 0.0027293851730408126
                        },
                        "99.9% VaR": {
                            "AAPL": 0.0029014731465457815,
                            "CSCO": 0.011908507707101083,
                            "NFLX": 0.006429076485202603,
                            "CVX": 0.006076103688970689,
                            "PFE": 0.029392658615313507,
                            "MMM": 0.021938512697046456,
                            "MSFT": 0.006799037615264997
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.00890440535495917,
                            "CSCO": 0.03654632472574231,
                            "NFLX": 0.019730357715160348,
                            "CVX": 0.018647110447935374,
                            "PFE": 0.09020388387266941,
                            "MMM": 0.067327664283912,
                            "MSFT": 0.020865740915785934
                        },
                        "95.0% DaR": {
                            "AAPL": 0.009387672710414288,
                            "CSCO": 0.038529797512274554,
                            "NFLX": 0.02080118023672027,
                            "CVX": 0.019659142065300415,
                            "PFE": 0.09509950471125211,
                            "MMM": 0.07098172774692979,
                            "MSFT": 0.02199818390664411
                        },
                        "99.0% DaR": {
                            "AAPL": 0.010492379079509034,
                            "CSCO": 0.04306384061589935,
                            "NFLX": 0.02324898567274708,
                            "CVX": 0.021972556701750537,
                            "PFE": 0.10629046031793088,
                            "MMM": 0.0793345931641906,
                            "MSFT": 0.024586848277444787
                        },
                        "99.9% DaR": {
                            "AAPL": 0.011438918328970508,
                            "CSCO": 0.04694871887531211,
                            "NFLX": 0.025346324825542187,
                            "CVX": 0.02395474655322489,
                            "PFE": 0.11587914290096205,
                            "MMM": 0.08649153113802123,
                            "MSFT": 0.026804878786903342
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 0.07817969640989349,
                            "CSCO": 0.32087269818244013,
                            "NFLX": 0.1732303634819092,
                            "CVX": 0.16371957201268106,
                            "PFE": 0.7919801463475624,
                            "MMM": 0.5911294627632779,
                            "MSFT": 0.18319890269316216
                        },
                        "95.0% ERM": {
                            "AAPL": 0.1017169335012338,
                            "CSCO": 0.41747651119369694,
                            "NFLX": 0.22538411086045207,
                            "CVX": 0.21300994483213326,
                            "PFE": 1.0304183257245034,
                            "MMM": 0.7690983594930325,
                            "MSFT": 0.23835383684581854
                        },
                        "99.0% ERM": {
                            "AAPL": 0.1563687055796419,
                            "CSCO": 0.64178361869778,
                            "NFLX": 0.3464813621523491,
                            "CVX": 0.32745864628909194,
                            "PFE": 1.5840546333136165,
                            "MMM": 1.182329340825958,
                            "MSFT": 0.36641962802653416
                        },
                        "99.9% ERM": {
                            "AAPL": 0.2345577147493903,
                            "CSCO": 0.9626945392131198,
                            "NFLX": 0.519732360822789,
                            "CVX": 0.4911977205655028,
                            "PFE": 2.3761291202796704,
                            "MMM": 1.7735292188886385,
                            "MSFT": 0.5496403533599061
                        }
                    }
                }
            }
        },
        {
            "name": "Max Sharpe",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.38988873214093406,
                    "annual_standard_deviation": 0.3370988612829789,
                    "annual_sharpe_ratio": 1.1566005612034402,
                    "annual_sortino_ratio": 1.6112402096193266,
                    "cvar_900": -0.03696999788812639,
                    "cvar_950": -0.04742727492462356,
                    "cvar_990": -0.0765520903058621,
                    "cvar_999": -0.12765606579445715,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.1880365383242459
                        }
                    ]
                },
                "weights": [
                    0.5770009677977765,
                    8.1463502612769e-11,
                    3.5501278942609523e-10,
                    0.2988088727647226,
                    0.052071698235098336,
                    1.4964702341551628e-10,
                    6.061918924872616e-11,
                    0.07211846055566
                ],
                "position": [
                    0.3370988612829789,
                    0.38988873214093406
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.00154717750849577,
                        "annual_mean_return": 0.38988873214093406,
                        "daily_variance": 0.0004509350884058771,
                        "annual_variance": 0.11363564227828103,
                        "daily_standard_deviation": 0.021235232242805283,
                        "annual_standard_deviation": 0.3370988612829789,
                        "daily_semi_variance": 0.00023235939907508796,
                        "annual_semi_variance": 0.05855456856692216,
                        "daily_semi_deviation": 0.015243339498780704,
                        "annual_semi_deviation": 0.24198051278341026,
                        "mean_absolute_deviation": 0.015207171585360503
                    },
                    "stats_moments": {
                        "skew": -0.10938893373223761,
                        "kurtosis": 7.5519830477055425,
                        "first_lower_partial_moment": 0.007603585792680252,
                        "fourth_central_moment": 1.5356387651516582e-06,
                        "fourth_lower_partial_moment": 8.167625176291247e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.03234876866463217,
                        "conditional_var_at_95": 0.04742727492462356,
                        "entropic_var_at_95": 0.07692219912587048,
                        "drawdown_at_risk_at_95": 0.30294585183443035,
                        "conditional_dar_at_95": 0.3398995564699478,
                        "entropic_dar_at_95": 0.3523600096275633,
                        "entropic_risk_measure_at_95": 2.994410565942437,
                        "worst_realization": 0.12874949535891966,
                        "average_drawdown": 0.09427577158057415,
                        "max_drawdown": 0.3865969523069712,
                        "ulcer_index": 0.13566142829447933,
                        "gini_mean_difference": 0.022454616819236266
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.07285898693290581,
                        "annual_sharpe_ratio": 1.1566005612034402,
                        "daily_sortino_ratio": 0.10149859278667427,
                        "annual_sortino_ratio": 1.6112402096193266,
                        "mean_absolute_deviation_ratio": 0.10173999154354202,
                        "calmar_ratio": 0.004002042693981866,
                        "value_at_risk_ratio_at_95": 0.047828018572692796,
                        "conditional_var_ratio_at_95": 0.0326221042839739,
                        "entropic_var_ratio_at_95": 0.020113537133332207,
                        "drawdown_at_risk_ratio_at_95": 0.00510710907288261,
                        "conditional_dar_ratio_at_95": 0.004551866806076764,
                        "entropic_dar_ratio_at_95": 0.004390899836025951,
                        "entropic_risk_measure_ratio_at_95": 0.0005166885016012571,
                        "worst_realization_ratio": 0.012016959788328854,
                        "average_drawdown_ratio": 0.016411189031462367,
                        "ulcer_index_ratio": 0.011404697178459027,
                        "gini_mean_difference_ratio": 0.06890242309413826
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 0.0008927229203343738,
                            "AMD": 0.00046231036757954884,
                            "CVX": 8.056416039062729e-05,
                            "MSFT": 0.00011158006019122006
                        },
                        "annual_mean_return": {
                            "AAPL": 0.2249661759242622,
                            "AMD": 0.1165022126300463,
                            "CVX": 0.020302168418438078,
                            "MSFT": 0.028118175168187456
                        },
                        "daily_variance": {
                            "AAPL": 0.00026018998259244293,
                            "AMD": 0.00013474340554376493,
                            "CVX": 2.3480955862274354e-05,
                            "MSFT": 3.2520744407394844e-05
                        },
                        "annual_variance": {
                            "AAPL": 0.06556787561329562,
                            "AMD": 0.03395533819702877,
                            "CVX": 0.0059172008772931375,
                            "MSFT": 0.008195227590663502
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.012252749563433571,
                            "AMD": 0.006345275813473498,
                            "CVX": 0.0011057546060147256,
                            "MSFT": 0.0015314522598834873
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.19450636932960277,
                            "AMD": 0.10072813081538368,
                            "CVX": 0.017553310191475022,
                            "MSFT": 0.024311050946517403
                        },
                        "daily_semi_variance": {
                            "AAPL": 0.00013407159822994533,
                            "AMD": 6.943105015881937e-05,
                            "CVX": 1.209934851855193e-05,
                            "MSFT": 1.6757402167771313e-05
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.03378604275394622,
                            "AMD": 0.01749662464002248,
                            "CVX": 0.0030490358266750863,
                            "MSFT": 0.004222865346278371
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.008795421648954914,
                            "AMD": 0.004554845095746446,
                            "CVX": 0.0007937465749890136,
                            "MSFT": 0.0010993261790903312
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.13962299015453009,
                            "AMD": 0.07230592430260367,
                            "CVX": 0.012600336248581267,
                            "MSFT": 0.017451262077695224
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.008774552727894734,
                            "AMD": 0.004544037802300113,
                            "CVX": 0.0007918632503143857,
                            "MSFT": 0.0010967178048512688
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.06311752067068872,
                            "AMD": -0.032686384002604534,
                            "CVX": -0.005696067551248135,
                            "MSFT": -0.00788896150769621
                        },
                        "kurtosis": {
                            "AAPL": 4.357501530136681,
                            "AMD": 2.256599543082626,
                            "CVX": 0.39324458259102923,
                            "MSFT": 0.5446373918952052
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.004387276363947367,
                            "AMD": 0.0022720189011500567,
                            "CVX": 0.00039593162515719286,
                            "MSFT": 0.0005483589024256344
                        },
                        "fourth_central_moment": {
                            "AAPL": 8.860650542533452e-07,
                            "AMD": 4.588624886855434e-07,
                            "CVX": 7.996331842881186e-08,
                            "MSFT": 1.1074790378395765e-07
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 4.712727634377456e-07,
                            "AMD": 2.440558873670769e-07,
                            "CVX": 4.253021137522906e-08,
                            "MSFT": 5.8903655449073074e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.018665270838630774,
                            "AMD": 0.009666099106256995,
                            "CVX": 0.00168445532127114,
                            "MSFT": 0.002332943398473259
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.027365583549217497,
                            "AMD": 0.014171690567694793,
                            "CVX": 0.0024696187495852513,
                            "MSFT": 0.0034203820581260127
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.04438418336946568,
                            "AMD": 0.022985035626250285,
                            "CVX": 0.0040054695430529795,
                            "MSFT": 0.005547510587101524
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.17480004981183875,
                            "AMD": 0.09052290855393981,
                            "CVX": 0.01577490498849957,
                            "MSFT": 0.021847988480152205
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.19612237316403555,
                            "AMD": 0.10156500338770068,
                            "CVX": 0.017699147146193677,
                            "MSFT": 0.024513032772017877
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.20331206669982843,
                            "AMD": 0.10528829735227341,
                            "CVX": 0.01834798410330924,
                            "MSFT": 0.0254116614721522
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 1.7277777956501013,
                            "AMD": 0.8947564463827117,
                            "CVX": 0.15592404348258732,
                            "MSFT": 0.21595228042703668
                        },
                        "worst_realization": {
                            "AAPL": 0.07428858347361757,
                            "AMD": 0.03847149160210681,
                            "CVX": 0.006704204874586752,
                            "MSFT": 0.00928521540860852
                        },
                        "average_drawdown": {
                            "AAPL": 0.05439721147705439,
                            "AMD": 0.02817043705323485,
                            "CVX": 0.00490909953179964,
                            "MSFT": 0.0067990235184852655
                        },
                        "max_drawdown": {
                            "AAPL": 0.22306681577306003,
                            "AMD": 0.11551859960783407,
                            "CVX": 0.020130759852156725,
                            "MSFT": 0.027880777073920355
                        },
                        "ulcer_index": {
                            "AAPL": 0.07827677546936816,
                            "AMD": 0.040536838492542505,
                            "CVX": 0.007064120960861226,
                            "MSFT": 0.009783693371707433
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.01295633564460697,
                            "AMD": 0.006709638744459178,
                            "CVX": 0.0011692500317522381,
                            "MSFT": 0.00161939239841788
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.042039706000241074,
                            "AMD": 0.021770911770281412,
                            "CVX": 0.0037938911837389145,
                            "MSFT": 0.005254477978644408
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.6673596436014464,
                            "AMD": 0.3456025101557613,
                            "CVX": 0.06022615544048174,
                            "MSFT": 0.08341225200575077
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.058564786305899806,
                            "AMD": 0.030328680117406588,
                            "CVX": 0.005285204098292997,
                            "MSFT": 0.007319922265074869
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 0.929687160906312,
                            "AMD": 0.48145287110092233,
                            "CVX": 0.08390001403381586,
                            "MSFT": 0.11620016357827632
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.05870407362232777,
                            "AMD": 0.030400812207879695,
                            "CVX": 0.005297774141523072,
                            "MSFT": 0.00733733157181148
                        },
                        "calmar_ratio": {
                            "AAPL": 0.002309182509089004,
                            "AMD": 0.0011958458669184193,
                            "CVX": 0.00020839315961978041,
                            "MSFT": 0.000288621158354662
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.027596813022141807,
                            "AMD": 0.01429143632551943,
                            "CVX": 0.002490486151910641,
                            "MSFT": 0.003449283073120917
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.018822985755626558,
                            "AMD": 0.009747774214611768,
                            "CVX": 0.0016986883711676115,
                            "MSFT": 0.002352655942567961
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.011605530399274989,
                            "AMD": 0.006010103362009376,
                            "CVX": 0.0010473460367246828,
                            "MSFT": 0.0014505573353231585
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 0.0029468068796078967,
                            "AMD": 0.0015260495061415011,
                            "CVX": 0.0002659358426688681,
                            "MSFT": 0.0003683168444643439
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 0.002626431554091492,
                            "AMD": 0.0013601381901786151,
                            "CVX": 0.00023702343488568326,
                            "MSFT": 0.00032827362692097365
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 0.0025335534565286287,
                            "AMD": 0.0013120398312742715,
                            "CVX": 0.00022864161138995832,
                            "MSFT": 0.00031666493683309214
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 0.00029812976566672154,
                            "AMD": 0.0001543911088338165,
                            "CVX": 2.690484775432629e-05,
                            "MSFT": 3.726277934639275e-05
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.006933797432337094,
                            "AMD": 0.0035907742107318505,
                            "CVX": 0.0006257435042058662,
                            "MSFT": 0.0008666446410540426
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.009469271959990222,
                            "AMD": 0.004903808898391551,
                            "CVX": 0.0008545584834781433,
                            "MSFT": 0.0011835496896024505
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 0.006580521313667333,
                            "AMD": 0.003407824710322339,
                            "CVX": 0.0005938619503234716,
                            "MSFT": 0.0008224892041458828
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.039756764834642036,
                            "AMD": 0.020588655388833,
                            "CVX": 0.0035878661853454633,
                            "MSFT": 0.004969136685317758
                        }
                    }
                },
                "allocation": {
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.5770009677977765,
                        "Shares": 3120,
                        "Purchase Value": 577007.237548872,
                        "Current Value": 707616.0095216159,
                        "Net Value": 130608.77197274391,
                        "Net Change": 0.22635551770125148,
                        "%Shares": 0.5349794238683128,
                        "%Purchase Value": 0.577026075130989,
                        "%Current Value": 0.5840124600585789
                    },
                    "AMD": {
                        "Company Name": "Advanced Micro Devices, Inc.",
                        "Sector": "Technology",
                        "Industry": "Semiconductors",
                        "Market Cap": 276598226944,
                        "Volume (3 Months Average)": 46165160.0,
                        "Current Price": 170.8999938965,
                        "Purchase Price": 138.5800018311,
                        "Price Diff": 32.319992065400015,
                        "Weight": 0.2988088727647226,
                        "Shares": 2157,
                        "Purchase Value": 298917.0639496827,
                        "Current Value": 368631.2868347505,
                        "Net Value": 69714.22288506781,
                        "Net Change": 0.23322262691835802,
                        "%Shares": 0.3698559670781893,
                        "%Purchase Value": 0.2989268227089701,
                        "%Current Value": 0.30424024016142026
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.07211846055566,
                        "Shares": 195,
                        "Purchase Value": 71926.548614505,
                        "Current Value": 81131.699523927,
                        "Net Value": 9205.15090942201,
                        "Net Change": 0.1279798778995724,
                        "%Shares": 0.03343621399176955,
                        "%Purchase Value": 0.07192889680388243,
                        "%Current Value": 0.06695993701405174
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.052071698235098336,
                        "Shares": 360,
                        "Purchase Value": 52116.503906232,
                        "Current Value": 54266.401977552,
                        "Net Value": 2149.89807132,
                        "Net Change": 0.04125177074786321,
                        "%Shares": 0.06172839506172839,
                        "%Purchase Value": 0.05211820535615861,
                        "%Current Value": 0.04478736276594905
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 32.64598070829166
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.38988873214093406,
                    "Expected Daily Return": 0.00154717750849577,
                    "Expected Current Return": 0.2955109041226921,
                    "Net Value": 211678.04383855395,
                    "Net Change": 0.21168495450149485,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.03696999788812639,
                        "95.0% CVaR": 0.04742727492462356,
                        "99.0% CVaR": 0.0765520903058621,
                        "99.9% CVaR": 0.12765606579445715
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.06420501562909144,
                        "95.0% EVaR": 0.07692219912587048,
                        "99.0% EVaR": 0.10274619176321982,
                        "99.9% EVaR": 0.12853981416929783
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.30912043724585453,
                        "95.0% CDaR": 0.3398995564699478,
                        "99.0% CDaR": 0.3745206552929582,
                        "99.9% CDaR": 0.3865836474081566
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.32927028641175216,
                        "95.0% EDaR": 0.3523600096275633,
                        "99.0% EDaR": 0.3784374057731271,
                        "99.9% EDaR": 0.3897184776829755
                    },
                    "VaR": {
                        "90.0% VaR": 0.022519087414464883,
                        "95.0% VaR": 0.03234876866463217,
                        "99.0% VaR": 0.05526037238156121,
                        "99.9% VaR": 0.11180926051239157
                    },
                    "DaR": {
                        "90.0% DaR": 0.24929450618633964,
                        "95.0% DaR": 0.30294585183443035,
                        "99.0% DaR": 0.36027610966792656,
                        "99.9% DaR": 0.3863908227876549
                    },
                    "ERM": {
                        "90.0% ERM": 2.3012633853824926,
                        "95.0% ERM": 2.994410565942437,
                        "99.0% ERM": 4.603848478376538,
                        "99.9% ERM": 6.906433571370584
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.021331724574726815,
                            "AMD": 0.011046963402209762,
                            "CVX": 0.001925090575027778,
                            "MSFT": 0.0026662193361620336
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.027365583549217497,
                            "AMD": 0.014171690567694793,
                            "CVX": 0.0024696187495852513,
                            "MSFT": 0.0034203820581260127
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.044170630221992246,
                            "AMD": 0.022874443826871777,
                            "CVX": 0.003986197348250891,
                            "MSFT": 0.005520818908747186
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.07365767355629596,
                            "AMD": 0.038144765146290845,
                            "CVX": 0.006647268140227902,
                            "MSFT": 0.009206358951642438
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.03704635617941658,
                            "AMD": 0.01918502835837798,
                            "CVX": 0.0033432642011800525,
                            "MSFT": 0.004630366890116819
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.04438418336946568,
                            "AMD": 0.022985035626250285,
                            "CVX": 0.0040054695430529795,
                            "MSFT": 0.005547510587101524
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.05928465212325568,
                            "AMD": 0.030701473761491686,
                            "CVX": 0.00535016869576011,
                            "MSFT": 0.007409897182712341
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.07416759722419854,
                            "AMD": 0.03840883700215543,
                            "CVX": 0.006693286418948126,
                            "MSFT": 0.009270093523995734
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.1783627915722847,
                            "AMD": 0.09236792946171023,
                            "CVX": 0.01609642613697803,
                            "MSFT": 0.02229329007488155
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.19612237316403555,
                            "AMD": 0.10156500338770068,
                            "CVX": 0.017699147146193677,
                            "MSFT": 0.024513032772017877
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.2160987807040546,
                            "AMD": 0.11191009490757109,
                            "CVX": 0.019501926557838927,
                            "MSFT": 0.027009853123493556
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.2230591388335626,
                            "AMD": 0.11551462398601446,
                            "CVX": 0.020130067043480155,
                            "MSFT": 0.027879817545099373
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.1899892740495062,
                            "AMD": 0.09838888318124528,
                            "CVX": 0.017145663002905986,
                            "MSFT": 0.023746466178094665
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.20331206669982843,
                            "AMD": 0.10528829735227341,
                            "CVX": 0.01834798410330924,
                            "MSFT": 0.0254116614721522
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.2183587495231961,
                            "AMD": 0.11308045470420797,
                            "CVX": 0.019705878407036366,
                            "MSFT": 0.027292323138686667
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.2248679389371847,
                            "AMD": 0.11645133908734764,
                            "CVX": 0.020293302979674348,
                            "MSFT": 0.028105896678768807
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.012993535240472438,
                            "AMD": 0.00672890313035837,
                            "CVX": 0.001172607125134191,
                            "MSFT": 0.001624041918499882
                        },
                        "95.0% VaR": {
                            "AAPL": 0.018665270838630774,
                            "AMD": 0.009666099106256995,
                            "CVX": 0.00168445532127114,
                            "MSFT": 0.002332943398473259
                        },
                        "99.0% VaR": {
                            "AAPL": 0.03188528836564791,
                            "AMD": 0.016512289590572313,
                            "CVX": 0.00287750143687282,
                            "MSFT": 0.003985292988468163
                        },
                        "99.9% VaR": {
                            "AAPL": 0.06451405156612763,
                            "AMD": 0.03340959911997234,
                            "CVX": 0.005822098077056148,
                            "MSFT": 0.00806351174923544
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.14384317142921627,
                            "AMD": 0.07449141042815507,
                            "CVX": 0.012981188306198418,
                            "MSFT": 0.017978736022769882
                        },
                        "95.0% DaR": {
                            "AAPL": 0.17480004981183875,
                            "AMD": 0.09052290855393981,
                            "CVX": 0.01577490498849957,
                            "MSFT": 0.021847988480152205
                        },
                        "99.0% DaR": {
                            "AAPL": 0.2078796640872561,
                            "AMD": 0.10765369828355693,
                            "CVX": 0.018760188876076476,
                            "MSFT": 0.02598255842103702
                        },
                        "99.9% DaR": {
                            "AAPL": 0.2229478788408459,
                            "AMD": 0.1154570062784838,
                            "CVX": 0.0201200263380226,
                            "MSFT": 0.02786591133030257
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 1.3278312013820508,
                            "AMD": 0.6876379185655966,
                            "CVX": 0.11983069264061756,
                            "MSFT": 0.16596357279422758
                        },
                        "95.0% ERM": {
                            "AAPL": 1.7277777956501013,
                            "AMD": 0.8947564463827117,
                            "CVX": 0.15592404348258732,
                            "MSFT": 0.21595228042703668
                        },
                        "99.0% ERM": {
                            "AAPL": 2.656425029335606,
                            "AMD": 1.3756707750929813,
                            "CVX": 0.23973020884118343,
                            "MSFT": 0.33202246510676664
                        },
                        "99.9% ERM": {
                            "AAPL": 3.985018857289162,
                            "AMD": 2.063703631620366,
                            "CVX": 0.35962972504174934,
                            "MSFT": 0.49808135741930576
                        }
                    }
                }
            }
        },
        {
            "name": "Max Sortino",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.4071905617718909,
                    "annual_standard_deviation": 0.3524709621084618,
                    "annual_sharpe_ratio": 1.1552456955208437,
                    "annual_sortino_ratio": 1.615272688221536,
                    "cvar_900": -0.03857217260995701,
                    "cvar_950": -0.04904523073549611,
                    "cvar_990": -0.07787278582693855,
                    "cvar_999": -0.12480794317287938,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.2097966393963891
                        }
                    ]
                },
                "weights": [
                    0.6562603210522815,
                    3.4966448016949483e-13,
                    7.795441273727302e-13,
                    0.3338836511058037,
                    0.00985602766722169,
                    1.0476781406648956e-11,
                    2.351485877743294e-12,
                    1.6073565958975823e-10
                ],
                "position": [
                    0.3524709621084618,
                    0.4071905617718909
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.0016158355625868685,
                        "annual_mean_return": 0.4071905617718909,
                        "daily_variance": 0.0004929991235304154,
                        "annual_variance": 0.12423577912966469,
                        "daily_standard_deviation": 0.02220358357406334,
                        "annual_standard_deviation": 0.3524709621084618,
                        "daily_semi_variance": 0.0002521756595717363,
                        "annual_semi_variance": 0.06354826621207754,
                        "daily_semi_deviation": 0.015880039659010185,
                        "annual_semi_deviation": 0.2520878144855034,
                        "mean_absolute_deviation": 0.016019802908987274
                    },
                    "stats_moments": {
                        "skew": -0.07413490216327556,
                        "kurtosis": 6.785344149980401,
                        "first_lower_partial_moment": 0.008009901454493637,
                        "fourth_central_moment": 1.649165246426099e-06,
                        "fourth_lower_partial_moment": 8.621834727441559e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.03374360642593737,
                        "conditional_var_at_95": 0.04904523073549611,
                        "entropic_var_at_95": 0.07675984387038487,
                        "drawdown_at_risk_at_95": 0.3338772142112647,
                        "conditional_dar_at_95": 0.37648427230074333,
                        "entropic_dar_at_95": 0.3902324425325327,
                        "entropic_risk_measure_at_95": 2.994362880662134,
                        "worst_realization": 0.12551992408854903,
                        "average_drawdown": 0.10653366424148085,
                        "max_drawdown": 0.4296062008492392,
                        "ulcer_index": 0.15134889143910674,
                        "gini_mean_difference": 0.02363909160608687
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.07277363841728565,
                        "annual_sharpe_ratio": 1.1552456955208437,
                        "daily_sortino_ratio": 0.10175261506164178,
                        "annual_sortino_ratio": 1.615272688221536,
                        "mean_absolute_deviation_ratio": 0.10086488402927656,
                        "calmar_ratio": 0.0037612016758433856,
                        "value_at_risk_ratio_at_95": 0.0478856806883819,
                        "conditional_var_ratio_at_95": 0.03294582446356848,
                        "entropic_var_ratio_at_95": 0.021050532167774284,
                        "drawdown_at_risk_ratio_at_95": 0.004839610173470627,
                        "conditional_dar_ratio_at_95": 0.004291907209595481,
                        "entropic_dar_ratio_at_95": 0.0041407002249746585,
                        "entropic_risk_measure_ratio_at_95": 0.0005396258326010119,
                        "worst_realization_ratio": 0.012873140055812688,
                        "average_drawdown_ratio": 0.015167370559265089,
                        "ulcer_index_ratio": 0.010676229916338561,
                        "gini_mean_difference_ratio": 0.0683543847417049
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 0.0010604087652561984,
                            "AMD": 0.0005395010773173512,
                            "CVX": 1.5925720013319014e-05
                        },
                        "annual_mean_return": {
                            "AAPL": 0.267223008844562,
                            "AMD": 0.13595427148397252,
                            "CVX": 0.004013281443356392
                        },
                        "daily_variance": {
                            "AAPL": 0.0003235357631430833,
                            "AMD": 0.0001646043473850515,
                            "CVX": 4.859013002280654e-06
                        },
                        "annual_variance": {
                            "AAPL": 0.08153101231205699,
                            "AMD": 0.041480295541032976,
                            "CVX": 0.001224471276574725
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.014571330887371484,
                            "AMD": 0.007413413552636191,
                            "CVX": 0.00021883913405566704
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.23131270679531443,
                            "AMD": 0.11768429175810725,
                            "CVX": 0.0034739635550401246
                        },
                        "daily_semi_variance": {
                            "AAPL": 0.00016549287934102897,
                            "AMD": 8.419732995253423e-05,
                            "CVX": 2.485450278173102e-06
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.0417042055939393,
                            "AMD": 0.021217727148038622,
                            "CVX": 0.0006263334700996217
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.01042143992676554,
                            "AMD": 0.005302085621981521,
                            "CVX": 0.000156514110263124
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.16543523009652483,
                            "AMD": 0.08416799991440595,
                            "CVX": 0.0024845844745726097
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.01051316100208284,
                            "AMD": 0.0053487502861824365,
                            "CVX": 0.00015789162072199966
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.048651794703349835,
                            "AMD": -0.024752431812970068,
                            "CVX": -0.000730675646955661
                        },
                        "kurtosis": {
                            "AAPL": 4.452952131094258,
                            "AMD": 2.2655154792006322,
                            "CVX": 0.06687653968551054
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.00525658050104142,
                            "AMD": 0.0026743751430912182,
                            "CVX": 7.894581036099983e-05
                        },
                        "fourth_central_moment": {
                            "AAPL": 1.0822817142769238e-06,
                            "AMD": 5.506293138497396e-07,
                            "CVX": 1.6254218299435608e-08
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 5.65816802727895e-07,
                            "AMD": 2.878689658531887e-07,
                            "CVX": 8.497704163072169e-09
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.022144589990415995,
                            "AMD": 0.011266438516937398,
                            "CVX": 0.0003325779185839774
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.032186438874182655,
                            "AMD": 0.016375400710154694,
                            "CVX": 0.00048339115115876634
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.050374439791101844,
                            "AMD": 0.02562885693423273,
                            "CVX": 0.000756547145050294
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.21911036782860302,
                            "AMD": 0.11147614332136571,
                            "CVX": 0.0032907030612959907
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.24707168945438213,
                            "AMD": 0.12570194344164304,
                            "CVX": 0.003710639404718174
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.25609406806615376,
                            "AMD": 0.1302922327154589,
                            "CVX": 0.003846141750920035
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 1.9650815457536528,
                            "AMD": 0.9997688115058181,
                            "CVX": 0.029512523402663266
                        },
                        "worst_realization": {
                            "AAPL": 0.08237374569519931,
                            "AMD": 0.041909050548529295,
                            "CVX": 0.0012371278448204232
                        },
                        "average_drawdown": {
                            "AAPL": 0.06991381671020365,
                            "AMD": 0.03556984878883924,
                            "CVX": 0.0010499987424379689
                        },
                        "max_drawdown": {
                            "AAPL": 0.28193350334462447,
                            "AMD": 0.1434384869022949,
                            "CVX": 0.004234210602319787
                        },
                        "ulcer_index": {
                            "AAPL": 0.09932427210408636,
                            "AMD": 0.050532920473332625,
                            "CVX": 0.0014916988616877575
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.015513397849504946,
                            "AMD": 0.007892706215643643,
                            "CVX": 0.0002329875409382815
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.047758451320213606,
                            "AMD": 0.024297928103261597,
                            "CVX": 0.0007172589938104549
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.7581419111692173,
                            "AMD": 0.3857176508121451,
                            "CVX": 0.011386133539481279
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.06677620383992759,
                            "AMD": 0.03397353463227929,
                            "CVX": 0.0010028765894348954
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 1.0600393731444286,
                            "AMD": 0.5393131427691072,
                            "CVX": 0.015920172308000156
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.06619362118751775,
                            "AMD": 0.03367713575394149,
                            "CVX": 0.000994127087817324
                        },
                        "calmar_ratio": {
                            "AAPL": 0.0024683274197625595,
                            "AMD": 0.0012558037482952374,
                            "CVX": 3.7070507785588956e-05
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.03142547218785435,
                            "AMD": 0.01598824590671666,
                            "CVX": 0.000471962593810884
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.02162103734357061,
                            "AMD": 0.011000072162508787,
                            "CVX": 0.0003247149574890856
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.013814629001158252,
                            "AMD": 0.007028428539124465,
                            "CVX": 0.0002074746274915679
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 0.0031760441267645544,
                            "AMD": 0.0016158667149294458,
                            "CVX": 4.769933177662681e-05
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 0.002816608403787774,
                            "AMD": 0.001432997649597396,
                            "CVX": 4.230115621031102e-05
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 0.0027173772594978308,
                            "AMD": 0.0013825121094906772,
                            "CVX": 4.0810855986150685e-05
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 0.0003541350222127097,
                            "AMD": 0.00018017224325130992,
                            "CVX": 5.31856713699223e-06
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.00844813102745445,
                            "AMD": 0.004298131003781964,
                            "CVX": 0.00012687802457627434
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.00995374347448108,
                            "AMD": 0.005064137060886774,
                            "CVX": 0.0001494900238972353
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 0.007006386073748284,
                            "AMD": 0.003564618625134842,
                            "CVX": 0.00010522521745543488
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.04485827048375886,
                            "AMD": 0.02282241155063819,
                            "CVX": 0.0006737027073078508
                        }
                    }
                },
                "allocation": {
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.6562603210522815,
                        "Shares": 3548,
                        "Purchase Value": 656160.7944946788,
                        "Current Value": 804686.4108277863,
                        "Net Value": 148525.61633310746,
                        "Net Change": 0.2263555177012514,
                        "%Shares": 0.5887819449054099,
                        "%Purchase Value": 0.6561720626597851,
                        "%Current Value": 0.655920004292796
                    },
                    "AMD": {
                        "Company Name": "Advanced Micro Devices, Inc.",
                        "Sector": "Technology",
                        "Industry": "Semiconductors",
                        "Market Cap": 276598226944,
                        "Volume (3 Months Average)": 46165160.0,
                        "Current Price": 170.8999938965,
                        "Purchase Price": 138.5800018311,
                        "Price Diff": 32.319992065400015,
                        "Weight": 0.3338836511058037,
                        "Shares": 2410,
                        "Purchase Value": 333977.804412951,
                        "Current Value": 411868.985290565,
                        "Net Value": 77891.18087761401,
                        "Net Change": 0.23322262691835802,
                        "%Shares": 0.3999336209757717,
                        "%Purchase Value": 0.33398353977092043,
                        "%Current Value": 0.33572470339339844
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.00985602766722169,
                        "Shares": 68,
                        "Purchase Value": 9844.2285156216,
                        "Current Value": 10250.3203735376,
                        "Net Value": 406.09185791599884,
                        "Net Change": 0.04125177074786309,
                        "%Shares": 0.011284434118818453,
                        "%Purchase Value": 0.009844397569294403,
                        "%Current Value": 0.008355292313805721
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 17.172576748604286
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.4071905617718909,
                    "Expected Daily Return": 0.0016158355625868685,
                    "Expected Current Return": 0.3086245924540919,
                    "Net Value": 226822.88906863728,
                    "Net Change": 0.22682678426899877,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.03857217260995701,
                        "95.0% CVaR": 0.04904523073549611,
                        "99.0% CVaR": 0.07787278582693855,
                        "99.9% CVaR": 0.12480794317287938
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.06430221231938925,
                        "95.0% EVaR": 0.07675984387038487,
                        "99.0% EVaR": 0.10186124914723961,
                        "99.9% EVaR": 0.12538323769062404
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.3411135394017881,
                        "95.0% CDaR": 0.37648427230074333,
                        "99.0% CDaR": 0.4142099508540011,
                        "99.9% CDaR": 0.42925569153536036
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.36452050205674996,
                        "95.0% EDaR": 0.3902324425325327,
                        "99.0% EDaR": 0.4190746408982159,
                        "99.9% EDaR": 0.4317226051068488
                    },
                    "VaR": {
                        "90.0% VaR": 0.024016416093630574,
                        "95.0% VaR": 0.03374360642593737,
                        "99.0% VaR": 0.05745456777835464,
                        "99.9% VaR": 0.11448937917766716
                    },
                    "DaR": {
                        "90.0% DaR": 0.27780644560345613,
                        "95.0% DaR": 0.3338772142112647,
                        "99.0% DaR": 0.4001989673797377,
                        "99.9% DaR": 0.4241758464066818
                    },
                    "ERM": {
                        "90.0% ERM": 2.3012157001021896,
                        "95.0% ERM": 2.994362880662134,
                        "99.0% ERM": 4.603800793096235,
                        "99.9% ERM": 6.90638588609028
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.02531338638511648,
                            "AMD": 0.01287861782434553,
                            "CVX": 0.00038016840049499975
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.032186438874182655,
                            "AMD": 0.016375400710154694,
                            "CVX": 0.00048339115115876634
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.05110481943694991,
                            "AMD": 0.026000450058220624,
                            "CVX": 0.0007675163317680152
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.08190650087081723,
                            "AMD": 0.04167133176084633,
                            "CVX": 0.0012301105412158234
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.04219899050846623,
                            "AMD": 0.02146945742712884,
                            "CVX": 0.0006337643837941781
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.050374439791101844,
                            "AMD": 0.02562885693423273,
                            "CVX": 0.000756547145050294
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.0668474960798317,
                            "AMD": 0.03400980577741958,
                            "CVX": 0.001003947289988338
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.08228404383579792,
                            "AMD": 0.041863413194925626,
                            "CVX": 0.0012357806599005063
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.22385928092220422,
                            "AMD": 0.11389223399698864,
                            "CVX": 0.0033620244825952623
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.24707168945438213,
                            "AMD": 0.12570194344164304,
                            "CVX": 0.003710639404718174
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.27182955537798326,
                            "AMD": 0.1382979307396491,
                            "CVX": 0.00408246473636875
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.2817034779897264,
                            "AMD": 0.14332145757281003,
                            "CVX": 0.004230755972823975
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.2392203417516917,
                            "AMD": 0.12170743615088976,
                            "CVX": 0.0035927241541684925
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.25609406806615376,
                            "AMD": 0.1302922327154589,
                            "CVX": 0.003846141750920035
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.2750220584287772,
                            "AMD": 0.13992217121339334,
                            "CVX": 0.004130411256045364
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.2833224154824424,
                            "AMD": 0.14414511968316493,
                            "CVX": 0.004255069941241457
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.015761020938884523,
                            "AMD": 0.00801868869321837,
                            "CVX": 0.0002367064615276822
                        },
                        "95.0% VaR": {
                            "AAPL": 0.022144589990415995,
                            "AMD": 0.011266438516937398,
                            "CVX": 0.0003325779185839774
                        },
                        "99.0% VaR": {
                            "AAPL": 0.03770515310272992,
                            "AMD": 0.019183140865894076,
                            "CVX": 0.0005662738097306513
                        },
                        "99.9% VaR": {
                            "AAPL": 0.07513483674933778,
                            "AMD": 0.03822613193935413,
                            "CVX": 0.001128410488975248
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.1823133472139662,
                            "AMD": 0.09275503037501144,
                            "CVX": 0.002738068014478503
                        },
                        "95.0% DaR": {
                            "AAPL": 0.21911036782860302,
                            "AMD": 0.11147614332136571,
                            "CVX": 0.0032907030612959907
                        },
                        "99.0% DaR": {
                            "AAPL": 0.26263470286329865,
                            "AMD": 0.13361989242086172,
                            "CVX": 0.0039443720955773
                        },
                        "99.9% DaR": {
                            "AAPL": 0.27836977719410155,
                            "AMD": 0.14162538033389852,
                            "CVX": 0.0041806888786817716
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 1.5101965544234346,
                            "AMD": 0.7683383000663406,
                            "CVX": 0.022680845612414298
                        },
                        "95.0% ERM": {
                            "AAPL": 1.9650815457536528,
                            "AMD": 0.9997688115058181,
                            "CVX": 0.029512523402663266
                        },
                        "99.0% ERM": {
                            "AAPL": 3.021291787065882,
                            "AMD": 1.5371338180312923,
                            "CVX": 0.04537518799906038
                        },
                        "99.9% ERM": {
                            "AAPL": 4.532387019708329,
                            "AMD": 2.305929335996244,
                            "CVX": 0.06806953038570646
                        }
                    }
                }
            }
        },
        {
            "name": "Target Return",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.2500000121455583,
                    "annual_standard_deviation": 0.25032817584065936,
                    "annual_sharpe_ratio": 0.9986890660869515,
                    "annual_sortino_ratio": 1.3767306050393064,
                    "cvar_900": -0.02770322248065516,
                    "cvar_950": -0.03683520745949863,
                    "cvar_990": -0.06337362261127764,
                    "cvar_999": -0.12132429181720973,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.09614296868301246
                        }
                    ]
                },
                "weights": [
                    0.3200720400367682,
                    7.380404623958638e-07,
                    0.05277738663364244,
                    0.07188139932548275,
                    0.15022660494915074,
                    0.23657686052829133,
                    1.938998955887138e-06,
                    0.1684630314872462
                ],
                "position": [
                    0.25032817584065936,
                    0.2500000121455583
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.000992063540260152,
                        "annual_mean_return": 0.2500000121455583,
                        "daily_variance": 0.0002486674429353653,
                        "annual_variance": 0.06266419561971205,
                        "daily_standard_deviation": 0.015769192843495997,
                        "annual_standard_deviation": 0.25032817584065936,
                        "daily_semi_variance": 0.00013085236752602872,
                        "annual_semi_variance": 0.032974796616559235,
                        "daily_semi_deviation": 0.011439071969614875,
                        "annual_semi_deviation": 0.18158963796582459,
                        "mean_absolute_deviation": 0.010725342618526326
                    },
                    "stats_moments": {
                        "skew": -0.25003849438228615,
                        "kurtosis": 12.712666391881829,
                        "first_lower_partial_moment": 0.005362671309263162,
                        "fourth_central_moment": 7.860940467748065e-07,
                        "fourth_lower_partial_moment": 4.421947871535863e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.022558226811379457,
                        "conditional_var_at_95": 0.03683520745949863,
                        "entropic_var_at_95": 0.0697528161560091,
                        "drawdown_at_risk_at_95": 0.1820246605809334,
                        "conditional_dar_at_95": 0.21609339273261344,
                        "entropic_dar_at_95": 0.245451270615974,
                        "entropic_risk_measure_at_95": 2.994864615969506,
                        "worst_realization": 0.12338925421355315,
                        "average_drawdown": 0.05976856878015984,
                        "max_drawdown": 0.3231400080227923,
                        "ulcer_index": 0.0854479904510685,
                        "gini_mean_difference": 0.015908475261497107
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.06291149776060533,
                        "annual_sharpe_ratio": 0.9986890660869515,
                        "daily_sortino_ratio": 0.086725876268226,
                        "annual_sortino_ratio": 1.3767306050393064,
                        "mean_absolute_deviation_ratio": 0.09249714210029242,
                        "calmar_ratio": 0.0030700733911914056,
                        "value_at_risk_ratio_at_95": 0.043977904316473464,
                        "conditional_var_ratio_at_95": 0.026932481413358522,
                        "entropic_var_ratio_at_95": 0.01422255895792513,
                        "drawdown_at_risk_ratio_at_95": 0.005450160088715298,
                        "conditional_dar_ratio_at_95": 0.004590901774991786,
                        "entropic_dar_ratio_at_95": 0.004041794274564201,
                        "entropic_risk_measure_ratio_at_95": 0.0003312548871058061,
                        "worst_realization_ratio": 0.008040112946490142,
                        "average_drawdown_ratio": 0.01659841553022878,
                        "ulcer_index_ratio": 0.011610144779569202,
                        "gini_mean_difference_ratio": 0.06236069289815719
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 0.0003175326512245893,
                            "NFLX": 5.235866119565005e-05,
                            "AMD": 7.131110639633491e-05,
                            "CVX": 0.00014903473651898212,
                            "PFE": 0.00023469990610022902,
                            "MSFT": 0.0001671264788243666
                        },
                        "annual_mean_return": {
                            "AAPL": 0.08001822810859649,
                            "NFLX": 0.013194382621303813,
                            "AMD": 0.017970398811876395,
                            "CVX": 0.03755675360278349,
                            "PFE": 0.059144376337257706,
                            "MSFT": 0.04211587266374038
                        },
                        "daily_variance": {
                            "AAPL": 7.95917088211909e-05,
                            "NFLX": 1.3124052912605968e-05,
                            "AMD": 1.7874611615923572e-05,
                            "CVX": 3.735656571856557e-05,
                            "PFE": 5.882912045312116e-05,
                            "MSFT": 4.189138341395814e-05
                        },
                        "annual_variance": {
                            "AAPL": 0.020057110622940105,
                            "NFLX": 0.0033072613339767036,
                            "AMD": 0.00450440212721274,
                            "CVX": 0.009413854561078523,
                            "PFE": 0.01482493835418653,
                            "MSFT": 0.010556628620317449
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.00504729123494856,
                            "NFLX": 0.0008322590155918466,
                            "AMD": 0.0011335146822873663,
                            "CVX": 0.0023689586454625224,
                            "PFE": 0.0037306361230394387,
                            "MSFT": 0.0026565331421662614
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.08012326441313983,
                            "NFLX": 0.013211702289884723,
                            "AMD": 0.017993987740636572,
                            "CVX": 0.03760605265254159,
                            "PFE": 0.0592220124818191,
                            "MSFT": 0.04217115626263754
                        },
                        "daily_semi_variance": {
                            "AAPL": 4.18822963382552e-05,
                            "NFLX": 6.906064480655536e-06,
                            "AMD": 9.405876462725356e-06,
                            "CVX": 1.9657559547055573e-05,
                            "PFE": 3.0956725174375566e-05,
                            "MSFT": 2.2043845522961486e-05
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.010554338677240309,
                            "NFLX": 0.001740328249125195,
                            "AMD": 0.0023702808686067896,
                            "CVX": 0.004953705005858004,
                            "PFE": 0.0078010947439426425,
                            "MSFT": 0.005555049071786294
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.003661336902985258,
                            "NFLX": 0.000603725940268566,
                            "AMD": 0.0008222587013797789,
                            "CVX": 0.0017184575461428272,
                            "PFE": 0.0027062269786049618,
                            "MSFT": 0.001927065900233483
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.05812192146793449,
                            "NFLX": 0.009583852187935567,
                            "AMD": 0.013052952223258907,
                            "CVX": 0.027279667834297347,
                            "PFE": 0.04296002146009466,
                            "MSFT": 0.030591222792303616
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.0034328914819908305,
                            "NFLX": 0.000566057069513335,
                            "AMD": 0.00077095469954103,
                            "CVX": 0.0016112361218402547,
                            "PFE": 0.002537374677433272,
                            "MSFT": 0.0018068285682076035
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.08003054522958458,
                            "NFLX": -0.013196413618627187,
                            "AMD": -0.0179731649763067,
                            "CVX": -0.03756253467403412,
                            "PFE": -0.059153480368380744,
                            "MSFT": -0.042122355515352816
                        },
                        "kurtosis": {
                            "AAPL": 4.068979959176221,
                            "NFLX": 0.6709431054500002,
                            "AMD": 0.9138066957030468,
                            "CVX": 1.9097858244755097,
                            "PFE": 3.0075307552133075,
                            "MSFT": 2.141620051863743
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.001716445740995415,
                            "NFLX": 0.0002830285347566675,
                            "AMD": 0.00038547734977051497,
                            "CVX": 0.0008056180609201273,
                            "PFE": 0.0012686873387166358,
                            "MSFT": 0.0009034142841038016
                        },
                        "fourth_central_moment": {
                            "AAPL": 2.516073987748955e-07,
                            "NFLX": 4.1488100502319005e-08,
                            "AMD": 5.650569135156769e-08,
                            "CVX": 1.180925559561454e-07,
                            "PFE": 1.8597215952076527e-07,
                            "MSFT": 1.324281406691137e-07
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 1.4153456651148647e-07,
                            "NFLX": 2.3337947725592053e-08,
                            "AMD": 3.178566516651238e-08,
                            "CVX": 6.642959943495184e-08,
                            "PFE": 1.0461333454079171e-07,
                            "MSFT": 7.449367377425186e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.007220277004096495,
                            "NFLX": 0.0011905674453895542,
                            "AMD": 0.0016215212503798832,
                            "CVX": 0.0033888548996445916,
                            "PFE": 0.00533676876486163,
                            "MSFT": 0.003800237447007304
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.01178995155890437,
                            "NFLX": 0.0019440711901755974,
                            "AMD": 0.0026477733448268368,
                            "CVX": 0.005533642973018477,
                            "PFE": 0.008714381066418104,
                            "MSFT": 0.006205387326155242
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.022325985932907872,
                            "NFLX": 0.0036813812022536657,
                            "AMD": 0.005013943454711345,
                            "CVX": 0.010478756808804552,
                            "PFE": 0.0165019464355568,
                            "MSFT": 0.01175080232177487
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.058261160416562645,
                            "NFLX": 0.00960681160615081,
                            "AMD": 0.013084222341282497,
                            "CVX": 0.027345019979791513,
                            "PFE": 0.043062938020147594,
                            "MSFT": 0.030664508216998326
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.069165638209534,
                            "NFLX": 0.011404875068524799,
                            "AMD": 0.015533137037431498,
                            "CVX": 0.03246306364706503,
                            "PFE": 0.05112283329142867,
                            "MSFT": 0.036403845478629446
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.07856229923004349,
                            "NFLX": 0.012954311288220015,
                            "AMD": 0.017643428030246266,
                            "CVX": 0.03687340977666448,
                            "PFE": 0.058068246465991916,
                            "MSFT": 0.04134957582480783
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 0.9585749934103348,
                            "NFLX": 0.15806155088943993,
                            "AMD": 0.21527563568762512,
                            "CVX": 0.44990954796503557,
                            "PFE": 0.7085175652827834,
                            "MSFT": 0.504525322734287
                        },
                        "worst_realization": {
                            "AAPL": 0.03949355604055364,
                            "NFLX": 0.006512179809427538,
                            "AMD": 0.008869415998374163,
                            "CVX": 0.018536398370378893,
                            "PFE": 0.029191120530549973,
                            "MSFT": 0.02078658346426894
                        },
                        "average_drawdown": {
                            "AAPL": 0.019130298952108032,
                            "NFLX": 0.0031544373076029617,
                            "AMD": 0.004296259860856249,
                            "CVX": 0.008978853207257184,
                            "PFE": 0.01413989821334435,
                            "MSFT": 0.010068821238991062
                        },
                        "max_drawdown": {
                            "AAPL": 0.10342835846714536,
                            "NFLX": 0.017054530795868432,
                            "AMD": 0.023227818136510786,
                            "CVX": 0.04854435628366073,
                            "PFE": 0.0764476532625003,
                            "MSFT": 0.054437291077106695
                        },
                        "ulcer_index": {
                            "AAPL": 0.027349585836635142,
                            "NFLX": 0.004509733701838716,
                            "AMD": 0.006142137565917668,
                            "CVX": 0.012836595869264613,
                            "PFE": 0.02021507143590828,
                            "MSFT": 0.014394866041504082
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.0050918717619632585,
                            "NFLX": 0.0008396099972968276,
                            "AMD": 0.0011435265241968183,
                            "CVX": 0.0023898826262622594,
                            "PFE": 0.003763587208428285,
                            "MSFT": 0.0026799971433496585
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.020136265335581563,
                            "NFLX": 0.0033203133296226626,
                            "AMD": 0.00452217859874465,
                            "CVX": 0.0094510060215575,
                            "PFE": 0.014883444474904178,
                            "MSFT": 0.010598290000194773
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.3196533024693563,
                            "NFLX": 0.052708340069966365,
                            "AMD": 0.07178735973898136,
                            "CVX": 0.15003006943449057,
                            "PFE": 0.2362673563958086,
                            "MSFT": 0.16824263797834835
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.0277586024520204,
                            "NFLX": 0.004577177356233806,
                            "AMD": 0.00623399403253652,
                            "CVX": 0.013028568831008041,
                            "PFE": 0.020517390459964976,
                            "MSFT": 0.01461014313646226
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 0.4406541529845224,
                            "NFLX": 0.0726604379473845,
                            "AMD": 0.09896158730851398,
                            "CVX": 0.2068221183956087,
                            "PFE": 0.3257034762544587,
                            "MSFT": 0.23192883214881813
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.029605828225580604,
                            "NFLX": 0.004881770499826158,
                            "AMD": 0.006648841806988645,
                            "CVX": 0.013895568824211571,
                            "PFE": 0.02188274206688952,
                            "MSFT": 0.015582390676795923
                        },
                        "calmar_ratio": {
                            "AAPL": 0.0009826472839667459,
                            "NFLX": 0.0001620308841236304,
                            "AMD": 0.00022068176216454466,
                            "CVX": 0.0004612079371752387,
                            "PFE": 0.0007263102688407272,
                            "MSFT": 0.000517195254920519
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.014076135233484333,
                            "NFLX": 0.002321045072977005,
                            "AMD": 0.0031612017643320328,
                            "CVX": 0.006606668944555599,
                            "PFE": 0.010404182388211253,
                            "MSFT": 0.0074086709129132415
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.00862035734626242,
                            "NFLX": 0.0014214297897797892,
                            "AMD": 0.0019359496339132478,
                            "CVX": 0.00404598607684917,
                            "PFE": 0.006371618956084022,
                            "MSFT": 0.004537139610469874
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.004552255646774117,
                            "NFLX": 0.0007506315025123102,
                            "AMD": 0.0010223401767297901,
                            "CVX": 0.002136612465734016,
                            "PFE": 0.003364737354478984,
                            "MSFT": 0.0023959818116959125
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 0.0017444485280795519,
                            "NFLX": 0.0002876459762569912,
                            "AMD": 0.0003917661824982661,
                            "CVX": 0.0008187612384131709,
                            "PFE": 0.0012893852148999046,
                            "MSFT": 0.0009181529485674133
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 0.001469423230433951,
                            "NFLX": 0.00024229644661295533,
                            "AMD": 0.00033000132717881303,
                            "CVX": 0.0006896774336057216,
                            "PFE": 0.0010861040364646348,
                            "MSFT": 0.0007733993006957098
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 0.0012936688020710708,
                            "NFLX": 0.0002133159101774173,
                            "AMD": 0.0002905306060032837,
                            "CVX": 0.0006071866572333112,
                            "PFE": 0.0009561975601561816,
                            "MSFT": 0.0006808947389229363
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 0.00010602571132311326,
                            "NFLX": 1.7482814053249068e-05,
                            "AMD": 2.381112856189991e-05,
                            "CVX": 4.976343028138391e-05,
                            "PFE": 7.836745101890067e-05,
                            "MSFT": 5.5804351867259264e-05
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.0025734222420619127,
                            "NFLX": 0.00042433728552270433,
                            "AMD": 0.0005779361164864067,
                            "CVX": 0.0012078421047998526,
                            "PFE": 0.0019021097711963432,
                            "MSFT": 0.001354465426422922
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.005312702942453495,
                            "NFLX": 0.0008760233390937496,
                            "AMD": 0.001193120528929356,
                            "CVX": 0.0024935302879203988,
                            "PFE": 0.003926811548114861,
                            "MSFT": 0.0027962268837169175
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 0.003716092672845516,
                            "NFLX": 0.0006127547402724826,
                            "AMD": 0.0008345556872653543,
                            "CVX": 0.0017441573023806375,
                            "PFE": 0.002746698955250786,
                            "MSFT": 0.001955885421554425
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.019959967627639703,
                            "NFLX": 0.0032912432106156925,
                            "AMD": 0.004482585868485299,
                            "CVX": 0.009368260255568755,
                            "PFE": 0.014753136440942737,
                            "MSFT": 0.010505499494905004
                        }
                    }
                },
                "allocation": {
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.3200720400367682,
                        "Shares": 1731,
                        "Purchase Value": 320128.0539093261,
                        "Current Value": 392590.80528266577,
                        "Net Value": 72462.75137333968,
                        "Net Change": 0.22635551770125156,
                        "%Shares": 0.14218827008378512,
                        "%Purchase Value": 0.320128524173836,
                        "%Current Value": 0.34251458773485666
                    },
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.23657686052829133,
                        "Shares": 8317,
                        "Purchase Value": 236639.88159934178,
                        "Current Value": 237699.8593654129,
                        "Net Value": 1059.977766071126,
                        "Net Change": 0.004479286242484642,
                        "%Shares": 0.6831772630195498,
                        "%Purchase Value": 0.2366402292206658,
                        "%Current Value": 0.20738047921565164
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.1684630314872462,
                        "Shares": 457,
                        "Purchase Value": 168566.321624763,
                        "Current Value": 190139.4188842802,
                        "Net Value": 21573.097259517206,
                        "Net Change": 0.12797987789957233,
                        "%Shares": 0.03753901757844587,
                        "%Purchase Value": 0.1685665692467932,
                        "%Current Value": 0.16588652560113834
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.15022660494915074,
                        "Shares": 1038,
                        "Purchase Value": 150269.2529296356,
                        "Current Value": 156468.12570194158,
                        "Net Value": 6198.872772305971,
                        "Net Change": 0.041251770747863015,
                        "%Shares": 0.08526367668802366,
                        "%Purchase Value": 0.15026947367347773,
                        "%Current Value": 0.13651011395913745
                    },
                    "AMD": {
                        "Company Name": "Advanced Micro Devices, Inc.",
                        "Sector": "Technology",
                        "Industry": "Semiconductors",
                        "Market Cap": 276598226944,
                        "Volume (3 Months Average)": 46165160.0,
                        "Current Price": 170.8999938965,
                        "Purchase Price": 138.5800018311,
                        "Price Diff": 32.319992065400015,
                        "Weight": 0.07188139932548275,
                        "Shares": 519,
                        "Purchase Value": 71923.0209503409,
                        "Current Value": 88697.09683228351,
                        "Net Value": 16774.075881942612,
                        "Net Change": 0.23322262691835816,
                        "%Shares": 0.04263183834401183,
                        "%Purchase Value": 0.07192312660444959,
                        "%Current Value": 0.07738349738709387
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.05277738663364244,
                        "Shares": 112,
                        "Purchase Value": 52472.0,
                        "Current Value": 80606.401367184,
                        "Net Value": 28134.401367183993,
                        "Net Change": 0.5361793216798291,
                        "%Shares": 0.00919993428618367,
                        "%Purchase Value": 0.052472077080777724,
                        "%Current Value": 0.07032479610212215
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 1.4689865926102854
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.2500000121455583,
                    "Expected Daily Return": 0.000992063540260152,
                    "Expected Current Return": 0.18948413618968904,
                    "Net Value": 146203.17642036057,
                    "Net Change": 0.14620339119118203,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.02770322248065516,
                        "95.0% CVaR": 0.03683520745949863,
                        "99.0% CVaR": 0.06337362261127764,
                        "99.9% CVaR": 0.12132429181720973
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.05755652233031415,
                        "95.0% EVaR": 0.0697528161560091,
                        "99.0% EVaR": 0.09503554115972737,
                        "99.9% EVaR": 0.1230095015703383
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.19056927338943488,
                        "95.0% CDaR": 0.21609339273261344,
                        "99.0% CDaR": 0.2662125280230419,
                        "99.9% CDaR": 0.32199346317703975
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.2215932665587696,
                        "95.0% EDaR": 0.245451270615974,
                        "99.0% EDaR": 0.28862684340851064,
                        "99.9% EDaR": 0.3229199291331392
                    },
                    "VaR": {
                        "90.0% VaR": 0.01530984036701068,
                        "95.0% VaR": 0.022558226811379457,
                        "99.0% VaR": 0.04369624770861803,
                        "99.9% VaR": 0.09139730056585611
                    },
                    "DaR": {
                        "90.0% DaR": 0.15083334824177308,
                        "95.0% DaR": 0.1820246605809334,
                        "99.0% DaR": 0.23940759199166461,
                        "99.9% DaR": 0.3053768712096111
                    },
                    "ERM": {
                        "90.0% ERM": 2.3017174354095613,
                        "95.0% ERM": 2.994864615969506,
                        "99.0% ERM": 4.604302528403606,
                        "99.9% ERM": 6.906887621397652
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.00886705067241993,
                            "NFLX": 0.0014621075979790261,
                            "AMD": 0.001991351728661738,
                            "CVX": 0.004161772200648046,
                            "PFE": 0.006553958946196626,
                            "MSFT": 0.004666981334749795
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.01178995155890437,
                            "NFLX": 0.0019440711901755974,
                            "AMD": 0.0026477733448268368,
                            "CVX": 0.005533642973018477,
                            "PFE": 0.008714381066418104,
                            "MSFT": 0.006205387326155242
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.020284178975258582,
                            "NFLX": 0.003344703136832085,
                            "AMD": 0.004555396868600675,
                            "CVX": 0.009520429654786439,
                            "PFE": 0.014992772813924613,
                            "MSFT": 0.010676141161875251
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.03883261754439838,
                            "NFLX": 0.006403196198898367,
                            "AMD": 0.008720983214410083,
                            "CVX": 0.018226185249775807,
                            "PFE": 0.02870259690191706,
                            "MSFT": 0.02043871270781003
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.018422282836862782,
                            "NFLX": 0.0030376909643333168,
                            "AMD": 0.004137254441004598,
                            "CVX": 0.008646544089502438,
                            "PFE": 0.01361657780794775,
                            "MSFT": 0.009696172190663264
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.022325985932907872,
                            "NFLX": 0.0036813812022536657,
                            "AMD": 0.005013943454711345,
                            "CVX": 0.010478756808804552,
                            "PFE": 0.0165019464355568,
                            "MSFT": 0.01175080232177487
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.030418300965982914,
                            "NFLX": 0.005015740927060545,
                            "AMD": 0.006831305971891081,
                            "CVX": 0.014276904917768356,
                            "PFE": 0.02248327015477597,
                            "MSFT": 0.016010018222248505
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.03937200751194031,
                            "NFLX": 0.00649213740369713,
                            "AMD": 0.008842118773906584,
                            "CVX": 0.018479349267345565,
                            "PFE": 0.029101279601933174,
                            "MSFT": 0.020722609011515538
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.06099605939093638,
                            "NFLX": 0.010057775147227043,
                            "AMD": 0.013698422710890628,
                            "CVX": 0.028628651588950137,
                            "PFE": 0.04508440110434907,
                            "MSFT": 0.032103963447081635
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.069165638209534,
                            "NFLX": 0.011404875068524799,
                            "AMD": 0.015533137037431498,
                            "CVX": 0.03246306364706503,
                            "PFE": 0.05112283329142867,
                            "MSFT": 0.036403845478629446
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.08520741503128912,
                            "NFLX": 0.014050039130700038,
                            "AMD": 0.019135780259508597,
                            "CVX": 0.03999231134082613,
                            "PFE": 0.06297989271264638,
                            "MSFT": 0.04484708954807164
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.10306138053695732,
                            "NFLX": 0.016994018993258857,
                            "AMD": 0.023145402667979216,
                            "CVX": 0.04837211428296275,
                            "PFE": 0.07617640655629913,
                            "MSFT": 0.05424414013958247
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.0709259987575712,
                            "NFLX": 0.01169514481294764,
                            "AMD": 0.01592847672250912,
                            "CVX": 0.03328929323146632,
                            "PFE": 0.05242397965774253,
                            "MSFT": 0.03733037337653278
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.07856229923004349,
                            "NFLX": 0.012954311288220015,
                            "AMD": 0.017643428030246266,
                            "CVX": 0.03687340977666448,
                            "PFE": 0.058068246465991916,
                            "MSFT": 0.04134957582480783
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.09238162988839958,
                            "NFLX": 0.015233011286790414,
                            "AMD": 0.020746956927522237,
                            "CVX": 0.04335954685766682,
                            "PFE": 0.06828261527302887,
                            "MSFT": 0.04862308317510271
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.10335791717939097,
                            "NFLX": 0.017042915576124907,
                            "AMD": 0.023211998515610774,
                            "CVX": 0.048511294490739446,
                            "PFE": 0.07639558755033565,
                            "MSFT": 0.054400215820937466
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.004900264957108822,
                            "NFLX": 0.0008080155274384865,
                            "AMD": 0.0011004956951008455,
                            "CVX": 0.002299951497710294,
                            "PFE": 0.003621963665356194,
                            "MSFT": 0.002579149024296037
                        },
                        "95.0% VaR": {
                            "AAPL": 0.007220277004096495,
                            "NFLX": 0.0011905674453895542,
                            "AMD": 0.0016215212503798832,
                            "CVX": 0.0033888548996445916,
                            "PFE": 0.00533676876486163,
                            "MSFT": 0.003800237447007304
                        },
                        "99.0% VaR": {
                            "AAPL": 0.013985984587081375,
                            "NFLX": 0.002306179933491734,
                            "AMD": 0.0031409558390309757,
                            "CVX": 0.006564356515323942,
                            "PFE": 0.010337548773796954,
                            "MSFT": 0.007361222059893051
                        },
                        "99.9% VaR": {
                            "AAPL": 0.029253798759539647,
                            "NFLX": 0.0048237235825335885,
                            "AMD": 0.00656978344681473,
                            "CVX": 0.013730342922194888,
                            "PFE": 0.021622544313034314,
                            "MSFT": 0.015397107541738942
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.04827766671853742,
                            "NFLX": 0.007960611248272995,
                            "AMD": 0.01084214116140576,
                            "CVX": 0.022659242479159833,
                            "PFE": 0.0356837755168828,
                            "MSFT": 0.02540991111751427
                        },
                        "95.0% DaR": {
                            "AAPL": 0.058261160416562645,
                            "NFLX": 0.00960681160615081,
                            "AMD": 0.013084222341282497,
                            "CVX": 0.027345019979791513,
                            "PFE": 0.043062938020147594,
                            "MSFT": 0.030664508216998326
                        },
                        "99.0% DaR": {
                            "AAPL": 0.07662788150492167,
                            "NFLX": 0.012635340870878978,
                            "AMD": 0.017208998790673204,
                            "CVX": 0.035965486024983055,
                            "PFE": 0.05663844812338433,
                            "MSFT": 0.04033143667682337
                        },
                        "99.9% DaR": {
                            "AAPL": 0.09774285980959421,
                            "NFLX": 0.016117036346743285,
                            "AMD": 0.02195097558781149,
                            "CVX": 0.04587585340328184,
                            "PFE": 0.07224529487222431,
                            "MSFT": 0.051444851189955954
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 0.7367173673611691,
                            "NFLX": 0.12147895621396061,
                            "AMD": 0.1654511130282521,
                            "CVX": 0.34578012154086,
                            "PFE": 0.5445345424328589,
                            "MSFT": 0.38775533483246055
                        },
                        "95.0% ERM": {
                            "AAPL": 0.9585749934103348,
                            "NFLX": 0.15806155088943993,
                            "AMD": 0.21527563568762512,
                            "CVX": 0.44990954796503557,
                            "PFE": 0.7085175652827834,
                            "MSFT": 0.504525322734287
                        },
                        "99.0% ERM": {
                            "AAPL": 1.4737124483989077,
                            "NFLX": 0.2430037052503123,
                            "AMD": 0.33096459466477546,
                            "CVX": 0.6916905886838356,
                            "PFE": 1.0892743531225797,
                            "MSFT": 0.7756568382831952
                        },
                        "99.9% ERM": {
                            "AAPL": 2.2107075294366467,
                            "NFLX": 0.3645284542866641,
                            "AMD": 0.4964780763012989,
                            "CVX": 1.0376010558268114,
                            "PFE": 1.6340141638123007,
                            "MSFT": 1.1635583417339301
                        }
                    }
                }
            }
        },
        {
            "name": "Target Volatility",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.2534373787838327,
                    "annual_standard_deviation": 0.2518043713007081,
                    "annual_sharpe_ratio": 1.00648522293195,
                    "annual_sortino_ratio": 1.3873808467913913,
                    "cvar_900": -0.027884984764741143,
                    "cvar_950": -0.03704586687003015,
                    "cvar_990": -0.06365222430282245,
                    "cvar_999": -0.12168741450127159,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.09652745294927728
                        }
                    ]
                },
                "weights": [
                    0.32605688308538966,
                    5.588551643040448e-08,
                    0.051249386422331414,
                    0.07609180186721312,
                    0.14948621328196748,
                    0.2287436570462111,
                    1.0589420008756099e-07,
                    0.16837189651717063
                ],
                "position": [
                    0.2518043713007081,
                    0.2534373787838327
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.0010057038840628283,
                        "annual_mean_return": 0.2534373787838327,
                        "daily_variance": 0.0002516088944688288,
                        "annual_variance": 0.06340544140614486,
                        "daily_standard_deviation": 0.015862184416681985,
                        "annual_standard_deviation": 0.2518043713007081,
                        "daily_semi_variance": 0.0001324187263251109,
                        "annual_semi_variance": 0.033369519033927944,
                        "daily_semi_deviation": 0.011507333588851542,
                        "annual_semi_deviation": 0.1826732575773694,
                        "mean_absolute_deviation": 0.010797279727424372
                    },
                    "stats_moments": {
                        "skew": -0.24898731435800914,
                        "kurtosis": 12.63445138585722,
                        "first_lower_partial_moment": 0.005398639863712186,
                        "fourth_central_moment": 7.998496658924005e-07,
                        "fourth_lower_partial_moment": 4.496233603640272e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.022771570139639447,
                        "conditional_var_at_95": 0.03704586687003015,
                        "entropic_var_at_95": 0.06999028252521274,
                        "drawdown_at_risk_at_95": 0.18280759448808442,
                        "conditional_dar_at_95": 0.21726854272526722,
                        "entropic_dar_at_95": 0.24623210191344133,
                        "entropic_risk_measure_at_95": 2.9948524475748695,
                        "worst_realization": 0.12374546943555517,
                        "average_drawdown": 0.059894377470412624,
                        "max_drawdown": 0.3234395418749255,
                        "ulcer_index": 0.08586434753170256,
                        "gini_mean_difference": 0.016013058756330058
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.06340260947950818,
                        "annual_sharpe_ratio": 1.00648522293195,
                        "daily_sortino_ratio": 0.08739677843676728,
                        "annual_sortino_ratio": 1.3873808467913913,
                        "mean_absolute_deviation_ratio": 0.0931441908936014,
                        "calmar_ratio": 0.003109403006920333,
                        "value_at_risk_ratio_at_95": 0.04416488972414583,
                        "conditional_var_ratio_at_95": 0.027147532748826992,
                        "entropic_var_ratio_at_95": 0.014369193090491407,
                        "drawdown_at_risk_ratio_at_95": 0.005501433826527273,
                        "conditional_dar_ratio_at_95": 0.004628851795331115,
                        "entropic_dar_ratio_at_95": 0.004084373549377271,
                        "entropic_risk_measure_ratio_at_95": 0.0003358108293038655,
                        "worst_realization_ratio": 0.00812719761499296,
                        "average_drawdown_ratio": 0.01679129037712494,
                        "ulcer_index_ratio": 0.0117127062974712,
                        "gini_mean_difference_ratio": 0.06280523286441246
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 0.00032791672679467103,
                            "NFLX": 5.1541715319179574e-05,
                            "AMD": 7.6525833063523e-05,
                            "CVX": 0.000150338889633302,
                            "PFE": 0.0002300484215632785,
                            "MSFT": 0.00016933229768887424
                        },
                        "annual_mean_return": {
                            "AAPL": 0.08263501515225709,
                            "NFLX": 0.012988512260433252,
                            "AMD": 0.019284509932007792,
                            "CVX": 0.0378854001875921,
                            "PFE": 0.057972202233946175,
                            "MSFT": 0.04267173901759631
                        },
                        "daily_variance": {
                            "AAPL": 8.203882515928495e-05,
                            "NFLX": 1.2894803546046277e-05,
                            "AMD": 1.9145377243284364e-05,
                            "CVX": 3.761206694707692e-05,
                            "PFE": 5.7553947977215494e-05,
                            "MSFT": 4.2363873595920817e-05
                        },
                        "annual_variance": {
                            "AAPL": 0.020673783940139807,
                            "NFLX": 0.0032494904936036617,
                            "AMD": 0.004824635065307659,
                            "CVX": 0.009478240870663384,
                            "PFE": 0.014503594890258304,
                            "MSFT": 0.010675696146172047
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.005171975246549658,
                            "NFLX": 0.000812927350187975,
                            "AMD": 0.00120698238908063,
                            "CVX": 0.002371178266438572,
                            "PFE": 0.0036283746592106823,
                            "MSFT": 0.0026707465052144687
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.0821025617361142,
                            "NFLX": 0.012904821615360591,
                            "AMD": 0.019160251430051695,
                            "CVX": 0.03764128804318629,
                            "PFE": 0.057598662069841204,
                            "MSFT": 0.04239678640615413
                        },
                        "daily_semi_variance": {
                            "AAPL": 4.3176044152711084e-05,
                            "NFLX": 6.786379572887122e-06,
                            "AMD": 1.0075981117128427e-05,
                            "CVX": 1.979477716835545e-05,
                            "PFE": 3.028994862130656e-05,
                            "MSFT": 2.2295595692722264e-05
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.010880363126483193,
                            "NFLX": 0.0017101676523675546,
                            "AMD": 0.0025391472415163636,
                            "CVX": 0.0049882838464255725,
                            "PFE": 0.007633067052569252,
                            "MSFT": 0.005618490114566011
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.003752045929609672,
                            "NFLX": 0.0005897438811943244,
                            "AMD": 0.0008756138891193849,
                            "CVX": 0.0017201880014613372,
                            "PFE": 0.002632229993806025,
                            "MSFT": 0.0019375118936607988
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.0595618826246361,
                            "NFLX": 0.009361893881173224,
                            "AMD": 0.013899939570743867,
                            "CVX": 0.027307137960863464,
                            "PFE": 0.04178535574281498,
                            "MSFT": 0.030757047797137775
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.0035205279432750695,
                            "NFLX": 0.0005533540505822383,
                            "AMD": 0.0008215846026397765,
                            "CVX": 0.001614044721318521,
                            "PFE": 0.0024698096505670736,
                            "MSFT": 0.0018179587590416938
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.08118404078130566,
                            "NFLX": -0.012760449152173964,
                            "AMD": -0.018945896456640902,
                            "CVX": -0.03722017680009529,
                            "PFE": -0.056954278058412564,
                            "MSFT": -0.04192247310938077
                        },
                        "kurtosis": {
                            "AAPL": 4.119550504826201,
                            "NFLX": 0.6475079860616159,
                            "AMD": 0.9613783270850972,
                            "CVX": 1.888676600116467,
                            "PFE": 2.8900510823251957,
                            "MSFT": 2.1272868854426448
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.0017602639716375347,
                            "NFLX": 0.00027667702529111915,
                            "AMD": 0.00041079230131988825,
                            "CVX": 0.0008070223606592605,
                            "PFE": 0.0012349048252835368,
                            "MSFT": 0.0009089793795208469
                        },
                        "fourth_central_moment": {
                            "AAPL": 2.607965311893553e-07,
                            "NFLX": 4.099181123873591e-08,
                            "AMD": 6.086201214688023e-08,
                            "CVX": 1.1956651709253906e-07,
                            "PFE": 1.8296056726272652e-07,
                            "MSFT": 1.3467222696216347e-07
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 1.4660281516003554e-07,
                            "NFLX": 2.3042925067681088e-08,
                            "AMD": 3.421265718660411e-08,
                            "CVX": 6.721250441755181e-08,
                            "PFE": 1.0284850838187657e-07,
                            "MSFT": 7.570395015027812e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.007424828383877802,
                            "NFLX": 0.0011670291863312564,
                            "AMD": 0.0017327300835913734,
                            "CVX": 0.003404036341363459,
                            "PFE": 0.0052088530731122015,
                            "MSFT": 0.0038340930713633564
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.012079061836985532,
                            "NFLX": 0.0018985782537238721,
                            "AMD": 0.002818887217912264,
                            "CVX": 0.005537847252060059,
                            "PFE": 0.008474008437220454,
                            "MSFT": 0.00623748387212797
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.022820817058381997,
                            "NFLX": 0.0035869596152400874,
                            "AMD": 0.005325687572126983,
                            "CVX": 0.010462583993862986,
                            "PFE": 0.016009835772581377,
                            "MSFT": 0.011784398513019307
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.05960568410611335,
                            "NFLX": 0.009368778566535042,
                            "AMD": 0.013910161509991149,
                            "CVX": 0.027327219480199033,
                            "PFE": 0.04181608446401951,
                            "MSFT": 0.030779666361226345
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.07084191529429042,
                            "NFLX": 0.011134881304941984,
                            "AMD": 0.016532357579629287,
                            "CVX": 0.03247865697167948,
                            "PFE": 0.04969880906433784,
                            "MSFT": 0.036581922510388214
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.080285684654056,
                            "NFLX": 0.012619246182082917,
                            "AMD": 0.018736247343289793,
                            "CVX": 0.03680831045833788,
                            "PFE": 0.05632404058594325,
                            "MSFT": 0.0414585726897315
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 0.976492412333578,
                            "NFLX": 0.15348437519428823,
                            "AMD": 0.2278837559293747,
                            "CVX": 0.4476892241532351,
                            "PFE": 0.685053611999851,
                            "MSFT": 0.5042490679645425
                        },
                        "worst_realization": {
                            "AAPL": 0.04034806858759458,
                            "NFLX": 0.006341880407103183,
                            "AMD": 0.009416017265576147,
                            "CVX": 0.018498244629361362,
                            "PFE": 0.02830599580092501,
                            "MSFT": 0.0208352627449949
                        },
                        "average_drawdown": {
                            "AAPL": 0.019528977191734923,
                            "NFLX": 0.0030695505920971824,
                            "AMD": 0.004557471840745214,
                            "CVX": 0.008953385133408879,
                            "PFE": 0.013700461155545102,
                            "MSFT": 0.010084531556881328
                        },
                        "max_drawdown": {
                            "AAPL": 0.10545970595154593,
                            "NFLX": 0.016576080747483547,
                            "AMD": 0.024611101517946044,
                            "CVX": 0.04834976016254746,
                            "PFE": 0.0739847556110544,
                            "MSFT": 0.054458137884348154
                        },
                        "ulcer_index": {
                            "AAPL": 0.02799666605364031,
                            "NFLX": 0.004400495838464553,
                            "AMD": 0.006533573976839588,
                            "CVX": 0.012835538244970806,
                            "PFE": 0.019640928041792228,
                            "MSFT": 0.014457145375995083
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.005221168871431405,
                            "NFLX": 0.0008206595687727293,
                            "AMD": 0.001218462691297258,
                            "CVX": 0.0023937319038027007,
                            "PFE": 0.003662886212999484,
                            "MSFT": 0.0026961495080264812
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.020672860570818144,
                            "NFLX": 0.003249345359077659,
                            "AMD": 0.004824419578872257,
                            "CVX": 0.009477817536605688,
                            "PFE": 0.014502947104898146,
                            "MSFT": 0.010675219329236292
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.32817148775218546,
                            "NFLX": 0.051581758463288156,
                            "AMD": 0.07658528655556174,
                            "CVX": 0.15045568904103282,
                            "PFE": 0.23022714790250806,
                            "MSFT": 0.16946385321737387
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.028496325778924244,
                            "NFLX": 0.004479031994789295,
                            "AMD": 0.006650179424507363,
                            "CVX": 0.013064615575145256,
                            "PFE": 0.01999146194789664,
                            "MSFT": 0.014715163715504487
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 0.452365147740675,
                            "NFLX": 0.07110242863508415,
                            "AMD": 0.10556832558723071,
                            "CVX": 0.20739434271897256,
                            "PFE": 0.31735461995247244,
                            "MSFT": 0.2335959821569565
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.03037030947357827,
                            "NFLX": 0.0047735834043705514,
                            "AMD": 0.00708751046517323,
                            "CVX": 0.013923774638481507,
                            "PFE": 0.02130614630451509,
                            "MSFT": 0.01568286660748276
                        },
                        "calmar_ratio": {
                            "AAPL": 0.0010138424167119209,
                            "NFLX": 0.00015935502202482968,
                            "AMD": 0.00023660011580499838,
                            "CVX": 0.0004648129562693922,
                            "PFE": 0.0007112563301002897,
                            "MSFT": 0.0005235361660089021
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.014400268614936321,
                            "NFLX": 0.0022634238659484753,
                            "AMD": 0.0033605865820517666,
                            "CVX": 0.006602043192954914,
                            "PFE": 0.010102440022913632,
                            "MSFT": 0.007436127445340726
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.008851641343557098,
                            "NFLX": 0.001391294621340781,
                            "AMD": 0.0020657050172965953,
                            "CVX": 0.0040581825271019676,
                            "PFE": 0.006209826925372506,
                            "MSFT": 0.004570882314158045
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.00468517506950404,
                            "NFLX": 0.0007364124484082859,
                            "AMD": 0.0010933779705197782,
                            "CVX": 0.0021479966105172545,
                            "PFE": 0.003286862308069805,
                            "MSFT": 0.0024193686834722426
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 0.0017937806561753372,
                            "NFLX": 0.00028194515366558863,
                            "AMD": 0.0004186140804369647,
                            "CVX": 0.0008223886433946881,
                            "PFE": 0.0012584182960641347,
                            "MSFT": 0.0009262869967905599
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 0.0015092692328190222,
                            "NFLX": 0.00023722585272895806,
                            "AMD": 0.0003522177306647136,
                            "CVX": 0.0006919496386709015,
                            "PFE": 0.0010588206588846652,
                            "MSFT": 0.0007793686815628544
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 0.0013317383243146115,
                            "NFLX": 0.00020932167218918587,
                            "AMD": 0.0003107873931499977,
                            "CVX": 0.0006105576343012782,
                            "PFE": 0.0009342746935740656,
                            "MSFT": 0.000687693831848132
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 0.00010949345002295754,
                            "NFLX": 1.721010174004276e-05,
                            "AMD": 2.5552455222123226e-05,
                            "CVX": 5.019909737290776e-05,
                            "PFE": 7.681460959773293e-05,
                            "MSFT": 5.6541115348101316e-05
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.0026499291512684046,
                            "NFLX": 0.0004165139584849346,
                            "AMD": 0.0006184132107024453,
                            "CVX": 0.001214904192606391,
                            "PFE": 0.0018590452047465408,
                            "MSFT": 0.001368391897184244
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.005474916689077525,
                            "NFLX": 0.0008605434682853294,
                            "AMD": 0.0012776797471737006,
                            "CVX": 0.0025100668206722455,
                            "PFE": 0.0038409017887684146,
                            "MSFT": 0.002827181863147724
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 0.0038190091256862886,
                            "NFLX": 0.0006002691082017424,
                            "AMD": 0.0008912410711007659,
                            "CVX": 0.0017508883949510518,
                            "PFE": 0.0026792077058332125,
                            "MSFT": 0.0019720908916981395
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.020478081782160675,
                            "NFLX": 0.0032187301691380373,
                            "AMD": 0.004778964108482515,
                            "CVX": 0.009388517954064968,
                            "PFE": 0.014366300971220691,
                            "MSFT": 0.010574637879345579
                        }
                    }
                },
                "allocation": {
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.32605688308538966,
                        "Shares": 1763,
                        "Purchase Value": 326046.0768585453,
                        "Current Value": 399848.40538032335,
                        "Net Value": 73802.32852177805,
                        "Net Change": 0.22635551770125148,
                        "%Shares": 0.14750669344042838,
                        "%Purchase Value": 0.32605333137106196,
                        "%Current Value": 0.34840245342744347
                    },
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.2287436570462111,
                        "Shares": 8040,
                        "Purchase Value": 228758.524475016,
                        "Current Value": 229783.19938654802,
                        "Net Value": 1024.6749115320272,
                        "Net Change": 0.004479286242484649,
                        "%Shares": 0.6726907630522089,
                        "%Purchase Value": 0.2287636143432797,
                        "%Current Value": 0.20021845615848585
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.16837189651717063,
                        "Shares": 456,
                        "Purchase Value": 168197.467529304,
                        "Current Value": 189723.3588867216,
                        "Net Value": 21525.891357417597,
                        "Net Change": 0.12797987789957227,
                        "%Shares": 0.03815261044176707,
                        "%Purchase Value": 0.16820120991640838,
                        "%Current Value": 0.1653128606221571
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.14948621328196748,
                        "Shares": 1034,
                        "Purchase Value": 149690.1806640108,
                        "Current Value": 155865.16567996878,
                        "Net Value": 6174.9850159579655,
                        "Net Change": 0.04125177074786298,
                        "%Shares": 0.08651271753681392,
                        "%Purchase Value": 0.14969351126470293,
                        "%Current Value": 0.13581098585381124
                    },
                    "AMD": {
                        "Company Name": "Advanced Micro Devices, Inc.",
                        "Sector": "Technology",
                        "Industry": "Semiconductors",
                        "Market Cap": 276598226944,
                        "Volume (3 Months Average)": 46165160.0,
                        "Current Price": 170.8999938965,
                        "Purchase Price": 138.5800018311,
                        "Price Diff": 32.319992065400015,
                        "Weight": 0.07609180186721312,
                        "Shares": 550,
                        "Purchase Value": 76219.00100710499,
                        "Current Value": 93994.996643075,
                        "Net Value": 17775.995635970015,
                        "Net Change": 0.2332226269183582,
                        "%Shares": 0.04601740294511379,
                        "%Purchase Value": 0.07622069687691009,
                        "%Current Value": 0.08190125807605181
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.051249386422331414,
                        "Shares": 109,
                        "Purchase Value": 51066.5,
                        "Current Value": 78447.301330563,
                        "Net Value": 27380.801330563,
                        "Net Change": 0.5361793216798293,
                        "%Shares": 0.009119812583668006,
                        "%Purchase Value": 0.05106763622763691,
                        "%Current Value": 0.0683539858620506
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 22.249466018932566
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.2534373787838327,
                    "Expected Daily Return": 0.0010057038840628283,
                    "Expected Current Return": 0.19208944185600021,
                    "Net Value": 147684.67677321855,
                    "Net Change": 0.14768796275152718,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.027884984764741143,
                        "95.0% CVaR": 0.03704586687003015,
                        "99.0% CVaR": 0.06365222430282245,
                        "99.9% CVaR": 0.12168741450127159
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.05775861605970608,
                        "95.0% EVaR": 0.06999028252521274,
                        "99.0% EVaR": 0.09534102008387267,
                        "99.9% EVaR": 0.12336674616793612
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.19186003826832124,
                        "95.0% CDaR": 0.21726854272526722,
                        "99.0% CDaR": 0.2670748030256148,
                        "99.9% CDaR": 0.3223038767718457
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.22242869961854703,
                        "95.0% EDaR": 0.24623210191344133,
                        "99.0% EDaR": 0.2891858228725973,
                        "99.9% EDaR": 0.3232215488330359
                    },
                    "VaR": {
                        "90.0% VaR": 0.015540712125708695,
                        "95.0% VaR": 0.022771570139639447,
                        "99.0% VaR": 0.043713682583770744,
                        "99.9% VaR": 0.09186053139571268
                    },
                    "DaR": {
                        "90.0% DaR": 0.1530169615690854,
                        "95.0% DaR": 0.18280759448808442,
                        "99.0% DaR": 0.24093950213808923,
                        "99.9% DaR": 0.3058449622344568
                    },
                    "ERM": {
                        "90.0% ERM": 2.3017052670149254,
                        "95.0% ERM": 2.9948524475748695,
                        "99.0% ERM": 4.60429036000897,
                        "99.9% ERM": 6.906875453003016
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.009092092688191254,
                            "NFLX": 0.0014290885907865902,
                            "AMD": 0.002121819079056229,
                            "CVX": 0.0041684214542725495,
                            "PFE": 0.006378514423679026,
                            "MSFT": 0.004695048528755496
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.012079061836985532,
                            "NFLX": 0.0018985782537238721,
                            "AMD": 0.002818887217912264,
                            "CVX": 0.005537847252060059,
                            "PFE": 0.008474008437220454,
                            "MSFT": 0.00623748387212797
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.020754249215246937,
                            "NFLX": 0.003262137967684019,
                            "AMD": 0.0048434132236237935,
                            "CVX": 0.009515131517358631,
                            "PFE": 0.014560044921673265,
                            "MSFT": 0.010717247457235813
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.0396770255019424,
                            "NFLX": 0.006236406337434133,
                            "AMD": 0.009259416131949912,
                            "CVX": 0.018190593740737365,
                            "PFE": 0.027835228712694417,
                            "MSFT": 0.02048874407651336
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.01883259737048576,
                            "NFLX": 0.0029600941125461407,
                            "AMD": 0.004394957880354629,
                            "CVX": 0.00863411819599769,
                            "PFE": 0.013211919200845733,
                            "MSFT": 0.009724929299476128
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.022820817058381997,
                            "NFLX": 0.0035869596152400874,
                            "AMD": 0.005325687572126983,
                            "CVX": 0.010462583993862986,
                            "PFE": 0.016009835772581377,
                            "MSFT": 0.011784398513019307
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.031086600867910538,
                            "NFLX": 0.004886169570660779,
                            "AMD": 0.007254671183698675,
                            "CVX": 0.014252170368490217,
                            "PFE": 0.021808657128699664,
                            "MSFT": 0.0160527509644128
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.04022458323942537,
                            "NFLX": 0.006322471068873809,
                            "AMD": 0.009387199525071848,
                            "CVX": 0.018441630713044232,
                            "PFE": 0.02821936524166627,
                            "MSFT": 0.020771496379854596
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.06255729618691405,
                            "NFLX": 0.00983271083094966,
                            "AMD": 0.014598978379967613,
                            "CVX": 0.028680435240777395,
                            "PFE": 0.043886773894511656,
                            "MSFT": 0.032303843735200864
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.07084191529429042,
                            "NFLX": 0.011134881304941984,
                            "AMD": 0.016532357579629287,
                            "CVX": 0.03247865697167948,
                            "PFE": 0.04969880906433784,
                            "MSFT": 0.036581922510388214
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.08708159191321163,
                            "NFLX": 0.013687421998275032,
                            "AMD": 0.02032220628327083,
                            "CVX": 0.03992400742622112,
                            "PFE": 0.06109167703236982,
                            "MSFT": 0.044967898372266404
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.10508941446790122,
                            "NFLX": 0.016517878598353523,
                            "AMD": 0.02452468669995482,
                            "CVX": 0.04817999385926684,
                            "PFE": 0.07372497938016963,
                            "MSFT": 0.05426692376619967
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.07252442023934,
                            "NFLX": 0.01139933622234898,
                            "AMD": 0.016925003279078577,
                            "CVX": 0.03325002941038913,
                            "PFE": 0.05087916241399611,
                            "MSFT": 0.03745074805339424
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.080285684654056,
                            "NFLX": 0.012619246182082917,
                            "AMD": 0.018736247343289793,
                            "CVX": 0.03680831045833788,
                            "PFE": 0.05632404058594325,
                            "MSFT": 0.0414585726897315
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.09429104329270092,
                            "NFLX": 0.014820598381929832,
                            "AMD": 0.02200467389673857,
                            "CVX": 0.043229300589678346,
                            "PFE": 0.06614943339143234,
                            "MSFT": 0.0486907733201173
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.10538862780827409,
                            "NFLX": 0.016564908736034962,
                            "AMD": 0.02459451403191063,
                            "CVX": 0.04831717320292166,
                            "PFE": 0.07393489107737486,
                            "MSFT": 0.054421433976519704
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.0050671569763991176,
                            "NFLX": 0.0007964520898584498,
                            "AMD": 0.0011825209792527315,
                            "CVX": 0.0023231225832114613,
                            "PFE": 0.0035548398998379955,
                            "MSFT": 0.0026166195971489403
                        },
                        "95.0% VaR": {
                            "AAPL": 0.007424828383877802,
                            "NFLX": 0.0011670291863312564,
                            "AMD": 0.0017327300835913734,
                            "CVX": 0.003404036341363459,
                            "PFE": 0.0052088530731122015,
                            "MSFT": 0.0038340930713633564
                        },
                        "99.0% VaR": {
                            "AAPL": 0.014253149397318842,
                            "NFLX": 0.002240299773113868,
                            "AMD": 0.003326253412170863,
                            "CVX": 0.006534593935222536,
                            "PFE": 0.009999229234841459,
                            "MSFT": 0.007360156831103179
                        },
                        "99.9% VaR": {
                            "AAPL": 0.02995176339104145,
                            "NFLX": 0.004707796632085591,
                            "AMD": 0.006989834485192923,
                            "CVX": 0.013731885209954872,
                            "PFE": 0.021012517289062702,
                            "MSFT": 0.015466734388375147
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.04989224161996555,
                            "NFLX": 0.007842026661305944,
                            "AMD": 0.011643338205693767,
                            "CVX": 0.02287392985341281,
                            "PFE": 0.03500166504197159,
                            "MSFT": 0.025763760186735745
                        },
                        "95.0% DaR": {
                            "AAPL": 0.05960568410611335,
                            "NFLX": 0.009368778566535042,
                            "AMD": 0.013910161509991149,
                            "CVX": 0.027327219480199033,
                            "PFE": 0.04181608446401951,
                            "MSFT": 0.030779666361226345
                        },
                        "99.0% DaR": {
                            "AAPL": 0.0785599957887048,
                            "NFLX": 0.012348003647135612,
                            "AMD": 0.018333523824668747,
                            "CVX": 0.036017139631508106,
                            "PFE": 0.05511339176218883,
                            "MSFT": 0.040567447483883134
                        },
                        "99.9% DaR": {
                            "AAPL": 0.09972287122667355,
                            "NFLX": 0.015674369190672038,
                            "AMD": 0.023272298033415347,
                            "CVX": 0.045719612652301275,
                            "PFE": 0.06996010646879616,
                            "MSFT": 0.05149570466259843
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 0.7504869665576799,
                            "NFLX": 0.11796100174326085,
                            "AMD": 0.17514092946867052,
                            "CVX": 0.3440732601212955,
                            "PFE": 0.5265005653966321,
                            "MSFT": 0.38754254372738656
                        },
                        "95.0% ERM": {
                            "AAPL": 0.976492412333578,
                            "NFLX": 0.15348437519428823,
                            "AMD": 0.2278837559293747,
                            "CVX": 0.4476892241532351,
                            "PFE": 0.685053611999851,
                            "MSFT": 0.5042490679645425
                        },
                        "99.0% ERM": {
                            "AAPL": 1.5012608064781792,
                            "NFLX": 0.23596709403540472,
                            "AMD": 0.3503488064922526,
                            "CVX": 0.6882780421178343,
                            "PFE": 1.0532023854378512,
                            "MSFT": 0.7752332254474482
                        },
                        "99.9% ERM": {
                            "AAPL": 2.252034646398679,
                            "NFLX": 0.35397318632754865,
                            "AMD": 0.5255566835158347,
                            "CVX": 1.0324828241143733,
                            "PFE": 1.5799042054790704,
                            "MSFT": 1.16292390716751
                        }
                    }
                }
            }
        },
        {
            "name": "CVaR 90%",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.10240155297625012,
                    "annual_standard_deviation": 0.21498858588409386,
                    "annual_sharpe_ratio": 0.47631157977594935,
                    "annual_sortino_ratio": 0.6691263031459296,
                    "cvar_900": -0.023342124814112308,
                    "cvar_950": -0.030583458103266594,
                    "cvar_990": -0.05547415523556773,
                    "cvar_999": -0.09937792103654655,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.11922611976299065
                        }
                    ]
                },
                "weights": [
                    0.047094793653182594,
                    0.11254769809967582,
                    0.04194093388222489,
                    1.3401668824172535e-09,
                    0.09523894243624197,
                    0.3706028730354854,
                    0.2157429011526534,
                    0.11683185640036876
                ],
                "position": [
                    0.21498858588409386,
                    0.10240155297625012
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.00040635536895337345,
                        "annual_mean_return": 0.10240155297625012,
                        "daily_variance": 0.00018341306373191425,
                        "annual_variance": 0.04622009206044239,
                        "daily_standard_deviation": 0.013543007927780086,
                        "annual_standard_deviation": 0.21498858588409386,
                        "daily_semi_variance": 9.293864595271147e-05,
                        "annual_semi_variance": 0.02342053878008329,
                        "daily_semi_deviation": 0.009640469177001267,
                        "annual_semi_deviation": 0.15303770378597326,
                        "mean_absolute_deviation": 0.009192997199731793
                    },
                    "stats_moments": {
                        "skew": -0.037438343555467324,
                        "kurtosis": 13.158927439579765,
                        "first_lower_partial_moment": 0.004596498599865897,
                        "fourth_central_moment": 4.426709503194368e-07,
                        "fourth_lower_partial_moment": 2.2515489882078414e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.018390533765315516,
                        "conditional_var_at_95": 0.030583458103266594,
                        "entropic_var_at_95": 0.058326795741390096,
                        "drawdown_at_risk_at_95": 0.25061372005589716,
                        "conditional_dar_at_95": 0.2686252051815315,
                        "entropic_dar_at_95": 0.28288453993701534,
                        "entropic_risk_measure_at_95": 2.995417568685622,
                        "worst_realization": 0.10042998295132127,
                        "average_drawdown": 0.10074566523457361,
                        "max_drawdown": 0.32906308473323687,
                        "ulcer_index": 0.13473397420835512,
                        "gini_mean_difference": 0.013616976156439704
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.0300048092063682,
                        "annual_sharpe_ratio": 0.47631157977594935,
                        "daily_sortino_ratio": 0.042150995090860614,
                        "annual_sortino_ratio": 0.6691263031459296,
                        "mean_absolute_deviation_ratio": 0.044202707792103856,
                        "calmar_ratio": 0.0012348859164278347,
                        "value_at_risk_ratio_at_95": 0.022095898582332518,
                        "conditional_var_ratio_at_95": 0.013286769847323803,
                        "entropic_var_ratio_at_95": 0.006966872837573244,
                        "drawdown_at_risk_ratio_at_95": 0.0016214410322896108,
                        "conditional_dar_ratio_at_95": 0.0015127224144092014,
                        "entropic_dar_ratio_at_95": 0.0014364707560330058,
                        "entropic_risk_measure_ratio_at_95": 0.00013565900567635405,
                        "worst_realization_ratio": 0.004046155908941408,
                        "average_drawdown_ratio": 0.004033477450441427,
                        "ulcer_index_ratio": 0.00301598294966775,
                        "gini_mean_difference_ratio": 0.029841821288730166
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 1.913722227636908e-05,
                            "CSCO": 4.573436144743835e-05,
                            "NFLX": 1.7042923684800905e-05,
                            "CVX": 3.8700855644273816e-05,
                            "PFE": 0.00015059646740933933,
                            "MMM": 8.76682863144478e-05,
                            "MSFT": 4.747525217670417e-05
                        },
                        "annual_mean_return": {
                            "AAPL": 0.004822580013645009,
                            "CSCO": 0.011525059084754465,
                            "NFLX": 0.004294816768569828,
                            "CVX": 0.009752615622357002,
                            "PFE": 0.03795030978715351,
                            "MMM": 0.02209240815124085,
                            "MSFT": 0.011963763548529452
                        },
                        "daily_variance": {
                            "AAPL": 8.637800401328626e-06,
                            "CSCO": 2.0642718152100782e-05,
                            "NFLX": 7.692515189425772e-06,
                            "CVX": 1.7468066242228692e-05,
                            "PFE": 6.797340846238374e-05,
                            "MMM": 3.95700665318502e-05,
                            "MSFT": 2.1428488752596448e-05
                        },
                        "annual_variance": {
                            "AAPL": 0.002176725701134814,
                            "CSCO": 0.005201964974329397,
                            "NFLX": 0.0019385138277352946,
                            "CVX": 0.00440195269304163,
                            "PFE": 0.017129298932520704,
                            "MMM": 0.00997165676602625,
                            "MSFT": 0.0053999791656543054
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.0006378051646569847,
                            "CSCO": 0.0015242343696600384,
                            "NFLX": 0.0005680064008266956,
                            "CVX": 0.0012898217541759932,
                            "PFE": 0.005019077654304059,
                            "MMM": 0.0029218078245883713,
                            "MSFT": 0.0015822547595679447
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.010124843103569908,
                            "CSCO": 0.02419647049138654,
                            "NFLX": 0.009016822078081858,
                            "CVX": 0.020475285582904585,
                            "PFE": 0.07967538770525973,
                            "MMM": 0.046382261295500785,
                            "MSFT": 0.025117515627390473
                        },
                        "daily_semi_variance": {
                            "AAPL": 4.376926359414953e-06,
                            "CSCO": 1.0460030680496619e-05,
                            "NFLX": 3.897933610230063e-06,
                            "CVX": 8.851378363854888e-06,
                            "PFE": 3.444332925226248e-05,
                            "MMM": 2.0050853133908776e-05,
                            "MSFT": 1.0858194552543697e-05
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.0011029854425725683,
                            "CSCO": 0.002635927731485148,
                            "NFLX": 0.0009822792697779757,
                            "CVX": 0.0022305473476914315,
                            "PFE": 0.008679718971570145,
                            "MMM": 0.005052814989745012,
                            "MSFT": 0.0027362650272410114
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.0004540159072191989,
                            "CSCO": 0.0010850126159264672,
                            "NFLX": 0.0004043302808881073,
                            "CVX": 0.0009181480902372606,
                            "PFE": 0.0035727855791948407,
                            "MMM": 0.00207986279150635,
                            "MSFT": 0.0011263139120290422
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.00720727909061625,
                            "CSCO": 0.01722404130665443,
                            "NFLX": 0.006418544224576945,
                            "CVX": 0.014575149080980093,
                            "PFE": 0.05671621278184448,
                            "MMM": 0.03301679824477431,
                            "MSFT": 0.017879679056526758
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.00043294230675586926,
                            "CSCO": 0.001034650674853184,
                            "NFLX": 0.00038556288825014845,
                            "CVX": 0.0008755313322951482,
                            "PFE": 0.0034069511785936586,
                            "MMM": 0.0019833238888163412,
                            "MSFT": 0.0010740349301674435
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.0017631510668246091,
                            "CSCO": -0.0042135993934796084,
                            "NFLX": -0.0015701990938242047,
                            "CVX": -0.0035655882515658872,
                            "PFE": -0.013874757701940235,
                            "MMM": -0.008077056863830872,
                            "MSFT": -0.004373991184001909
                        },
                        "kurtosis": {
                            "AAPL": 0.6197169732947357,
                            "CSCO": 1.4810069947701605,
                            "NFLX": 0.551897706444045,
                            "CVX": 1.2532423346203765,
                            "PFE": 4.876736321709386,
                            "MMM": 2.838945185676857,
                            "MSFT": 1.537381923064204
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.00021647115337793463,
                            "CSCO": 0.000517325337426592,
                            "NFLX": 0.00019278144412507422,
                            "CVX": 0.0004377656661475741,
                            "PFE": 0.0017034755892968293,
                            "MMM": 0.0009916619444081706,
                            "MSFT": 0.0005370174650837217
                        },
                        "fourth_central_moment": {
                            "AAPL": 2.0847497089491252e-08,
                            "CSCO": 4.982159654081784e-08,
                            "NFLX": 1.8566033083810747e-08,
                            "CVX": 4.215951321217017e-08,
                            "PFE": 1.640551262175932e-07,
                            "MMM": 9.550311520590754e-08,
                            "MSFT": 5.171806896964608e-08
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 1.0603623514178662e-08,
                            "CSCO": 2.53406656121054e-08,
                            "NFLX": 9.443206737357019e-09,
                            "CVX": 2.144351447676844e-08,
                            "PFE": 8.344305249282427e-08,
                            "MMM": 4.85755711454275e-08,
                            "MSFT": 2.6305264842122867e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.000866098394010138,
                            "CSCO": 0.0020698122448845196,
                            "NFLX": 0.0007713161617436151,
                            "CVX": 0.0017514949889939448,
                            "PFE": 0.006815584659216056,
                            "MMM": 0.003967627113592284,
                            "MSFT": 0.002148600202874959
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.0014403216505043672,
                            "CSCO": 0.0034420978140635196,
                            "NFLX": 0.0012826987959179302,
                            "CVX": 0.0029127362097017785,
                            "PFE": 0.011334317455620876,
                            "MMM": 0.006598163987322004,
                            "MSFT": 0.0035731221901361184
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.0027468884135733855,
                            "CSCO": 0.00656454660702102,
                            "NFLX": 0.002446280287030103,
                            "CVX": 0.0055549823495493,
                            "PFE": 0.02161607810568224,
                            "MMM": 0.012583592145049846,
                            "MSFT": 0.0068144278334842006
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.011802601448506403,
                            "CSCO": 0.028205997342288538,
                            "NFLX": 0.010510973476929263,
                            "CVX": 0.02386818569012341,
                            "PFE": 0.0928781647992986,
                            "MMM": 0.05406813110597851,
                            "MSFT": 0.029279666192772443
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.012650848625022313,
                            "CSCO": 0.030233148535251955,
                            "NFLX": 0.011266391984716557,
                            "CVX": 0.025583580487493842,
                            "PFE": 0.09955327294344035,
                            "MMM": 0.05795398116625841,
                            "MSFT": 0.03138398143934806
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.013322389053863456,
                            "CSCO": 0.03183800384056514,
                            "NFLX": 0.011864441801702303,
                            "CVX": 0.026941624451270477,
                            "PFE": 0.1048378233784796,
                            "MMM": 0.06103033141903618,
                            "MSFT": 0.03304992599209819
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 0.14106857249142274,
                            "CSCO": 0.3371273526547014,
                            "NFLX": 0.12563061036626452,
                            "CVX": 0.28528040177888125,
                            "PFE": 1.1101103583835934,
                            "MMM": 0.6462400772979332,
                            "MSFT": 0.3499601957128255
                        },
                        "worst_realization": {
                            "AAPL": 0.004729729330023749,
                            "CSCO": 0.011303163416509025,
                            "NFLX": 0.004212127280399294,
                            "CVX": 0.009564845377992142,
                            "PFE": 0.03721964027054502,
                            "MMM": 0.02166705591366705,
                            "MSFT": 0.011733421362184996
                        },
                        "average_drawdown": {
                            "AAPL": 0.004744596322033408,
                            "CSCO": 0.011338692730867541,
                            "NFLX": 0.004225367290186713,
                            "CVX": 0.009594910624835244,
                            "PFE": 0.03733663303184153,
                            "MMM": 0.021735162125389677,
                            "MSFT": 0.011770303109419502
                        },
                        "max_drawdown": {
                            "AAPL": 0.015497158095160312,
                            "CSCO": 0.03703529276593787,
                            "NFLX": 0.013801213098373587,
                            "CVX": 0.03133962022680129,
                            "PFE": 0.12195172477549265,
                            "MMM": 0.07099302465773245,
                            "MSFT": 0.03844505111373871
                        },
                        "ulcer_index": {
                            "AAPL": 0.006345268721919431,
                            "CSCO": 0.015163998673293756,
                            "NFLX": 0.005650868711535125,
                            "CVX": 0.012831921231032562,
                            "PFE": 0.04993279800402369,
                            "MMM": 0.029067898518493153,
                            "MSFT": 0.015741220348057403
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.0006412886831272693,
                            "CSCO": 0.0015325593235393457,
                            "NFLX": 0.0005711086974184516,
                            "CVX": 0.0012968664100568583,
                            "PFE": 0.005046490492395397,
                            "MMM": 0.0029377659448539067,
                            "MSFT": 0.0015908966050484764
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.0014130703000707742,
                            "CSCO": 0.0033769722126224095,
                            "NFLX": 0.0012584297207595676,
                            "CVX": 0.002857626300645421,
                            "PFE": 0.01111986851166412,
                            "MMM": 0.0064733245953890566,
                            "MSFT": 0.003505517565216852
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.02243179559423211,
                            "CSCO": 0.053607771953846584,
                            "NFLX": 0.019976952501493634,
                            "CVX": 0.04536341118879167,
                            "PFE": 0.1765224401616072,
                            "MMM": 0.10276084221118353,
                            "MSFT": 0.05564836616479462
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.0019850924187407486,
                            "CSCO": 0.004743997476444848,
                            "NFLX": 0.0017678521005449884,
                            "CVX": 0.004014416200468781,
                            "PFE": 0.015621279902912712,
                            "MMM": 0.009093777979560702,
                            "MSFT": 0.004924579012187835
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 0.031512365216806296,
                            "CSCO": 0.0753086252579464,
                            "NFLX": 0.02806378207671116,
                            "CVX": 0.06372688155329526,
                            "PFE": 0.24798013070182948,
                            "MMM": 0.1443592500717182,
                            "MSFT": 0.07817526826762279
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.0020817174051709067,
                            "CSCO": 0.004974913018441108,
                            "NFLX": 0.0018539028474084745,
                            "CVX": 0.004209819148580065,
                            "PFE": 0.016381650525655878,
                            "MMM": 0.009536420430651883,
                            "MSFT": 0.005164284416195544
                        },
                        "calmar_ratio": {
                            "AAPL": 5.8156697497329856e-05,
                            "CSCO": 0.00013898356749592267,
                            "NFLX": 5.179226864240081e-05,
                            "CVX": 0.00011760922886761249,
                            "PFE": 0.0004576522691125444,
                            "MMM": 0.00026641787055973863,
                            "MSFT": 0.00014427401425228588
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.00104060178571118,
                            "CSCO": 0.0024868425262182,
                            "NFLX": 0.0009267226227519181,
                            "CVX": 0.0021043900159800418,
                            "PFE": 0.008188803507887506,
                            "MMM": 0.004767033270115841,
                            "MSFT": 0.0025815048536678327
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.000625737685115636,
                            "CSCO": 0.001495395363500555,
                            "NFLX": 0.000557259536421768,
                            "CVX": 0.001265417910348739,
                            "PFE": 0.004924115085378596,
                            "MMM": 0.0028665262776508597,
                            "MSFT": 0.0015523179889076499
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.0003281034391331881,
                            "CSCO": 0.0007841055018728578,
                            "NFLX": 0.000292197153438121,
                            "CVX": 0.0006635176020274805,
                            "PFE": 0.002581943093137764,
                            "MMM": 0.001503053359954013,
                            "MSFT": 0.0008139526880098196
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 7.636143093881967e-05,
                            "CSCO": 0.00018248945603312422,
                            "NFLX": 6.800475122032277e-05,
                            "CVX": 0.00015442432934494542,
                            "PFE": 0.0006009107058294738,
                            "MMM": 0.00034981439282292354,
                            "MSFT": 0.00018943596610000138
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 7.124135005662082e-05,
                            "CSCO": 0.00017025342583370755,
                            "NFLX": 6.34449908499228e-05,
                            "CVX": 0.0001440700831410089,
                            "PFE": 0.0005606192736365498,
                            "MMM": 0.0003263591227606633,
                            "MSFT": 0.00017673416813072829
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 6.76502939348683e-05,
                            "CSCO": 0.00016167147719568263,
                            "NFLX": 6.024692508327085e-05,
                            "CVX": 0.00013680795582851794,
                            "PFE": 0.0005323601899307394,
                            "MMM": 0.0003099083687428351,
                            "MSFT": 0.00016782554531709159
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 6.388832888085924e-06,
                            "CSCO": 1.5268108835826324e-05,
                            "NFLX": 5.689665395225439e-06,
                            "CVX": 1.2920020249883093e-05,
                            "PFE": 5.0275617324171764e-05,
                            "MMM": 2.92674674913242e-05,
                            "MSFT": 1.5849293491837313e-05
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.0001905528778755738,
                            "CSCO": 0.0004553855343140498,
                            "NFLX": 0.00016969955768151093,
                            "CVX": 0.0003853516102161667,
                            "PFE": 0.0014995170066127953,
                            "MMM": 0.000872929415480842,
                            "MSFT": 0.0004727199067604699
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.00018995578848787653,
                            "CSCO": 0.00045395860299251233,
                            "NFLX": 0.00016916781129112205,
                            "CVX": 0.00038414412723528844,
                            "PFE": 0.001494818333460744,
                            "MMM": 0.0008701941280582469,
                            "MSFT": 0.0004712386589156369
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 0.00014203709486647313,
                            "CSCO": 0.00033944193894788467,
                            "NFLX": 0.00012649314165145468,
                            "CVX": 0.00028723902691704244,
                            "PFE": 0.0011177319476708537,
                            "MMM": 0.0006506769122602733,
                            "MSFT": 0.0003523628873537684
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.0014053944177113622,
                            "CSCO": 0.0033586282976496053,
                            "NFLX": 0.0012515938552731482,
                            "CVX": 0.0028421035037188864,
                            "PFE": 0.011059464721036442,
                            "MMM": 0.006438161109137872,
                            "MSFT": 0.0034864753842028503
                        }
                    }
                },
                "allocation": {
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.3706028730354854,
                        "Shares": 13026,
                        "Purchase Value": 370622.9527128804,
                        "Current Value": 372283.0790061162,
                        "Net Value": 1660.1262932358077,
                        "Net Change": 0.004479286242484551,
                        "%Shares": 0.6833849220922302,
                        "%Purchase Value": 0.370623690476677,
                        "%Current Value": 0.31731719896129523
                    },
                    "MMM": {
                        "Company Name": "3M Company",
                        "Sector": "Industrials",
                        "Industry": "Conglomerates",
                        "Market Cap": 74311114752,
                        "Volume (3 Months Average)": 4169252.3076923075,
                        "Current Price": 135.2700042725,
                        "Purchase Price": 89.3647994995,
                        "Price Diff": 45.905204772999994,
                        "Weight": 0.2157429011526534,
                        "Shares": 2414,
                        "Purchase Value": 215726.625991793,
                        "Current Value": 326541.790313815,
                        "Net Value": 110815.164322022,
                        "Net Change": 0.5136832962206427,
                        "%Shares": 0.1266460311631079,
                        "%Purchase Value": 0.21572705541823153,
                        "%Current Value": 0.2783294006346285
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.11683185640036876,
                        "Shares": 317,
                        "Purchase Value": 116926.74826050301,
                        "Current Value": 131891.0192260762,
                        "Net Value": 14964.270965573189,
                        "Net Change": 0.1279798778995722,
                        "%Shares": 0.016630816851162057,
                        "%Purchase Value": 0.11692698101543923,
                        "%Current Value": 0.11241791837732508
                    },
                    "CSCO": {
                        "Company Name": "Cisco Systems, Inc.",
                        "Sector": "Technology",
                        "Industry": "Communication Equipment",
                        "Market Cap": 210511003648,
                        "Volume (3 Months Average)": 18805300.0,
                        "Current Price": 52.75,
                        "Purchase Price": 48.9177017212,
                        "Price Diff": 3.8322982788000033,
                        "Weight": 0.11254769809967582,
                        "Shares": 2302,
                        "Purchase Value": 112608.5493622024,
                        "Current Value": 121430.5,
                        "Net Value": 8821.950637797607,
                        "Net Change": 0.0783417483642564,
                        "%Shares": 0.12077015896332827,
                        "%Purchase Value": 0.11260877352131153,
                        "%Current Value": 0.10350184658227919
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.09523894243624197,
                        "Shares": 658,
                        "Purchase Value": 95257.3876952796,
                        "Current Value": 99186.92361452559,
                        "Net Value": 3929.5359192459873,
                        "Net Change": 0.04125177074786308,
                        "%Shares": 0.03452074917370547,
                        "%Purchase Value": 0.09525757731508454,
                        "%Current Value": 0.08454243168659334
                    },
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.047094793653182594,
                        "Shares": 255,
                        "Purchase Value": 47159.2453765905,
                        "Current Value": 57834.000778208996,
                        "Net Value": 10674.755401618495,
                        "Net Change": 0.2263555177012515,
                        "%Shares": 0.013378101883426892,
                        "%Purchase Value": 0.04715933925200663,
                        "%Current Value": 0.049295077231713634
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.04194093388222489,
                        "Shares": 89,
                        "Purchase Value": 41696.5,
                        "Current Value": 64053.301086423,
                        "Net Value": 22356.801086423002,
                        "Net Change": 0.5361793216798293,
                        "%Shares": 0.00466921987303919,
                        "%Purchase Value": 0.04169658300124944,
                        "%Current Value": 0.05459612652616509
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 1.9906007511440933
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.10240155297625012,
                    "Expected Daily Return": 0.00040635536895337345,
                    "Expected Current Return": 0.07761387547009432,
                    "Net Value": 173222.60462591588,
                    "Net Change": 0.17322294944364913,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.023342124814112308,
                        "95.0% CVaR": 0.030583458103266594,
                        "99.0% CVaR": 0.05547415523556773,
                        "99.9% CVaR": 0.09937792103654655
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.0483307590363833,
                        "95.0% EVaR": 0.058326795741390096,
                        "99.0% EVaR": 0.07886660893689822,
                        "99.9% EVaR": 0.10022876379403528
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.2551586912355075,
                        "95.0% CDaR": 0.2686252051815315,
                        "99.0% CDaR": 0.2942585473050373,
                        "99.9% CDaR": 0.3271957574741686
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.2684916114039552,
                        "95.0% EDaR": 0.28288453993701534,
                        "99.0% EDaR": 0.3073040938272487,
                        "99.9% EDaR": 0.32878549949179076
                    },
                    "VaR": {
                        "90.0% VaR": 0.013841438109095766,
                        "95.0% VaR": 0.018390533765315516,
                        "99.0% VaR": 0.03498550259402004,
                        "99.9% VaR": 0.08413064690937674
                    },
                    "DaR": {
                        "90.0% DaR": 0.23322223475629805,
                        "95.0% DaR": 0.25061372005589716,
                        "99.0% DaR": 0.27773984408465574,
                        "99.9% DaR": 0.3001330435746285
                    },
                    "ERM": {
                        "90.0% ERM": 2.3022703881256774,
                        "95.0% ERM": 2.995417568685622,
                        "99.0% ERM": 4.604855481119722,
                        "99.9% ERM": 6.907440574113767
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.001099292553020688,
                            "CSCO": 0.00262710242010442,
                            "NFLX": 0.0009789905148113363,
                            "CVX": 0.0022230792844901153,
                            "PFE": 0.008650658530456245,
                            "MMM": 0.005035897733212874,
                            "MSFT": 0.002727103778016629
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.0014403216505043672,
                            "CSCO": 0.0034420978140635196,
                            "NFLX": 0.0012826987959179302,
                            "CVX": 0.0029127362097017785,
                            "PFE": 0.011334317455620876,
                            "MMM": 0.006598163987322004,
                            "MSFT": 0.0035731221901361184
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.0026125438974049266,
                            "CSCO": 0.0062434884841545465,
                            "NFLX": 0.0023266378800253095,
                            "CVX": 0.005283299884259891,
                            "PFE": 0.02055888133707025,
                            "MMM": 0.011968155205553367,
                            "MSFT": 0.006481148547099437
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.00468018269117066,
                            "CSCO": 0.011184756269584107,
                            "NFLX": 0.004168002821132586,
                            "CVX": 0.009464648113717267,
                            "PFE": 0.03682974310179577,
                            "MMM": 0.02144008102367715,
                            "MSFT": 0.011610507015469014
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.0022761271269705523,
                            "CSCO": 0.005439515684244908,
                            "NFLX": 0.002027037171939264,
                            "CVX": 0.00460297038393474,
                            "PFE": 0.017911518178873827,
                            "MMM": 0.0104270181833931,
                            "MSFT": 0.00564657230702691
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.0027468884135733855,
                            "CSCO": 0.00656454660702102,
                            "NFLX": 0.002446280287030103,
                            "CVX": 0.0055549823495493,
                            "PFE": 0.02161607810568224,
                            "MMM": 0.012583592145049846,
                            "MSFT": 0.0068144278334842006
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.0037142066789871255,
                            "CSCO": 0.008876255304670882,
                            "NFLX": 0.0033077392353706584,
                            "CVX": 0.007511172438749083,
                            "PFE": 0.02922819189775123,
                            "MMM": 0.01701491103892103,
                            "MSFT": 0.00921413234244821
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.004720252955319598,
                            "CSCO": 0.01128051666351258,
                            "NFLX": 0.004203687961016414,
                            "CVX": 0.009545681478228629,
                            "PFE": 0.03714506787264511,
                            "MMM": 0.021623644308848496,
                            "MSFT": 0.011709912554464451
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.01201664592865667,
                            "CSCO": 0.02871752338716858,
                            "NFLX": 0.01070159381292538,
                            "CVX": 0.0243010439392528,
                            "PFE": 0.09456254417858302,
                            "MMM": 0.05504867637523693,
                            "MSFT": 0.02981066361368412
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.012650848625022313,
                            "CSCO": 0.030233148535251955,
                            "NFLX": 0.011266391984716557,
                            "CVX": 0.025583580487493842,
                            "PFE": 0.09955327294344035,
                            "MMM": 0.05795398116625841,
                            "MSFT": 0.03138398143934806
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.013858045584588098,
                            "CSCO": 0.033118122189720337,
                            "NFLX": 0.01234147829333976,
                            "CVX": 0.028024872885714647,
                            "PFE": 0.10905306319264445,
                            "MMM": 0.06348419276963348,
                            "MSFT": 0.034378772389396545
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.015409216703093673,
                            "CSCO": 0.03682512938104931,
                            "NFLX": 0.013722895649159572,
                            "CVX": 0.031161777953226926,
                            "PFE": 0.12125968792745705,
                            "MMM": 0.07059016205691973,
                            "MSFT": 0.038226887803262374
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.012644557053625577,
                            "CSCO": 0.030218112863085154,
                            "NFLX": 0.011260788936916644,
                            "CVX": 0.025570857157384365,
                            "PFE": 0.09950376270558457,
                            "MMM": 0.057925159257069536,
                            "MSFT": 0.03136837343028937
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.013322389053863456,
                            "CSCO": 0.03183800384056514,
                            "NFLX": 0.011864441801702303,
                            "CVX": 0.026941624451270477,
                            "PFE": 0.1048378233784796,
                            "MMM": 0.06103033141903618,
                            "MSFT": 0.03304992599209819
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.014472422906968006,
                            "CSCO": 0.03458636842321516,
                            "NFLX": 0.012888620698218578,
                            "CVX": 0.02926731694165794,
                            "PFE": 0.11388778022057341,
                            "MMM": 0.06629867682722916,
                            "MSFT": 0.03590290780938647
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.015484085275475718,
                            "CSCO": 0.037004051185944804,
                            "NFLX": 0.013789570914099812,
                            "CVX": 0.031313183301934625,
                            "PFE": 0.12184885088736261,
                            "MMM": 0.07093313761234545,
                            "MSFT": 0.03841262031462775
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.0006518596724847639,
                            "CSCO": 0.0015578219996556,
                            "NFLX": 0.0005805228413464912,
                            "CVX": 0.0013182439290736448,
                            "PFE": 0.005129676737048372,
                            "MMM": 0.002986192017783214,
                            "MSFT": 0.0016171209117036808
                        },
                        "95.0% VaR": {
                            "AAPL": 0.000866098394010138,
                            "CSCO": 0.0020698122448845196,
                            "NFLX": 0.0007713161617436151,
                            "CVX": 0.0017514949889939448,
                            "PFE": 0.006815584659216056,
                            "MMM": 0.003967627113592284,
                            "MSFT": 0.002148600202874959
                        },
                        "99.0% VaR": {
                            "AAPL": 0.0016476350277263645,
                            "CSCO": 0.0039375377890941525,
                            "NFLX": 0.0014673246530986625,
                            "CVX": 0.0033319822721202823,
                            "PFE": 0.012965727793310499,
                            "MMM": 0.007547873838032978,
                            "MSFT": 0.004087421220637107
                        },
                        "99.9% VaR": {
                            "AAPL": 0.0039621154614157585,
                            "CSCO": 0.009468710661976614,
                            "NFLX": 0.003528517904223782,
                            "CVX": 0.008012513848864039,
                            "PFE": 0.031179059496734152,
                            "MMM": 0.018150589864403276,
                            "MSFT": 0.009829139671759123
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.010983553035901764,
                            "CSCO": 0.026248625702661104,
                            "NFLX": 0.009781558340887552,
                            "CVX": 0.02221183902057436,
                            "PFE": 0.08643283037227494,
                            "MMM": 0.050316041607060845,
                            "MSFT": 0.0272477866769375
                        },
                        "95.0% DaR": {
                            "AAPL": 0.011802601448506403,
                            "CSCO": 0.028205997342288538,
                            "NFLX": 0.010510973476929263,
                            "CVX": 0.02386818569012341,
                            "PFE": 0.0928781647992986,
                            "MMM": 0.05406813110597851,
                            "MSFT": 0.029279666192772443
                        },
                        "99.0% DaR": {
                            "AAPL": 0.013080100663963489,
                            "CSCO": 0.03125898016418313,
                            "NFLX": 0.01164866845282516,
                            "CVX": 0.02645164905847898,
                            "PFE": 0.10293118431214618,
                            "MMM": 0.059920399808812606,
                            "MSFT": 0.03244886162424621
                        },
                        "99.9% DaR": {
                            "AAPL": 0.014134703774591655,
                            "CSCO": 0.03377928322324403,
                            "NFLX": 0.012587860153304254,
                            "CVX": 0.02858435369852596,
                            "PFE": 0.11123016839070887,
                            "MMM": 0.06475157363934403,
                            "MSFT": 0.035065100694909715
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 0.10842494900791894,
                            "CSCO": 0.25911523293384997,
                            "NFLX": 0.09655937025678897,
                            "CVX": 0.21926579726121867,
                            "PFE": 0.8532280214873663,
                            "MMM": 0.49669849343773803,
                            "MSFT": 0.2689785237407966
                        },
                        "95.0% ERM": {
                            "AAPL": 0.14106857249142274,
                            "CSCO": 0.3371273526547014,
                            "NFLX": 0.12563061036626452,
                            "CVX": 0.28528040177888125,
                            "PFE": 1.1101103583835934,
                            "MMM": 0.6462400772979332,
                            "MSFT": 0.3499601957128255
                        },
                        "99.0% ERM": {
                            "AAPL": 0.21686471897669515,
                            "CSCO": 0.5182658851762629,
                            "NFLX": 0.19313193952967225,
                            "CVX": 0.4385615666813204,
                            "PFE": 1.7065726735032642,
                            "MMM": 0.9934648822168756,
                            "MSFT": 0.5379938150356322
                        },
                        "99.9% ERM": {
                            "AAPL": 0.32530448894547137,
                            "CSCO": 0.7774165374186759,
                            "NFLX": 0.28970450880255555,
                            "CVX": 0.657857336101422,
                            "PFE": 2.5599173255191623,
                            "MMM": 1.490231270996013,
                            "MSFT": 0.8070091063304676
                        }
                    }
                }
            }
        },
        {
            "name": "CVaR 95%",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.07630328664819717,
                    "annual_standard_deviation": 0.21516233506997043,
                    "annual_sharpe_ratio": 0.35463124446657207,
                    "annual_sortino_ratio": 0.499707403394602,
                    "cvar_900": -0.02351963411278474,
                    "cvar_950": -0.030293790646711498,
                    "cvar_990": -0.054679874226695714,
                    "cvar_999": -0.0946207973035179,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.13565643143435355
                        }
                    ]
                },
                "weights": [
                    2.7116795171457734e-09,
                    0.12613621648019097,
                    0.057873613718560604,
                    3.374876195828467e-10,
                    0.101036755834969,
                    0.4015643092231909,
                    0.2531621174168733,
                    0.060226984277048035
                ],
                "position": [
                    0.21516233506997043,
                    0.07630328664819717
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.0003027908200325285,
                        "annual_mean_return": 0.07630328664819717,
                        "daily_variance": 0.00018370964457445327,
                        "annual_variance": 0.046294830432762224,
                        "daily_standard_deviation": 0.01355395309769269,
                        "annual_standard_deviation": 0.21516233506997043,
                        "daily_semi_variance": 9.252399608528478e-05,
                        "annual_semi_variance": 0.023316047013491763,
                        "daily_semi_deviation": 0.009618939447012066,
                        "annual_semi_deviation": 0.1526959299178985,
                        "mean_absolute_deviation": 0.009303285013392905
                    },
                    "stats_moments": {
                        "skew": -0.01782585309936047,
                        "kurtosis": 11.973043743904308,
                        "first_lower_partial_moment": 0.004651642506696452,
                        "fourth_central_moment": 4.040810491345433e-07,
                        "fourth_lower_partial_moment": 2.0447797424410094e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.019406465549482048,
                        "conditional_var_at_95": 0.030293790646711498,
                        "entropic_var_at_95": 0.056414203498895685,
                        "drawdown_at_risk_at_95": 0.29091594176724767,
                        "conditional_dar_at_95": 0.30753010064624736,
                        "entropic_dar_at_95": 0.3150141007586991,
                        "entropic_risk_measure_at_95": 2.9955212716605697,
                        "worst_realization": 0.09541465228707574,
                        "average_drawdown": 0.11238478298225023,
                        "max_drawdown": 0.34314620649150684,
                        "ulcer_index": 0.15048262177818592,
                        "gini_mean_difference": 0.013754772767611171
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.022339668571235725,
                        "annual_sharpe_ratio": 0.35463124446657207,
                        "daily_sortino_ratio": 0.031478607563808346,
                        "annual_sortino_ratio": 0.499707403394602,
                        "mean_absolute_deviation_ratio": 0.03254665632587137,
                        "calmar_ratio": 0.0008823959417427592,
                        "value_at_risk_ratio_at_95": 0.015602574268894104,
                        "conditional_var_ratio_at_95": 0.009995144667225642,
                        "entropic_var_ratio_at_95": 0.005367279891463072,
                        "drawdown_at_risk_ratio_at_95": 0.0010408189327581832,
                        "conditional_dar_ratio_at_95": 0.0009845892138565958,
                        "entropic_dar_ratio_at_95": 0.0009611976711622389,
                        "entropic_risk_measure_ratio_at_95": 0.00010108117839025598,
                        "worst_realization_ratio": 0.003173420567750081,
                        "average_drawdown_ratio": 0.0026942332582548163,
                        "ulcer_index_ratio": 0.0020121314770741275,
                        "gini_mean_difference_ratio": 0.02201350943037898
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "CSCO": 3.819288854029406e-05,
                            "NFLX": 1.752359900952114e-05,
                            "CVX": 3.059300224597981e-05,
                            "PFE": 0.00012158998685623402,
                            "MMM": 7.665516536756075e-05,
                            "MSFT": 1.8236178012938733e-05
                        },
                        "annual_mean_return": {
                            "CSCO": 0.009624607912154103,
                            "NFLX": 0.004415946950399327,
                            "CVX": 0.007709436565986911,
                            "PFE": 0.030640676687770974,
                            "MMM": 0.01931710167262531,
                            "MSFT": 0.00459551685926056
                        },
                        "daily_variance": {
                            "CSCO": 2.3172439568198824e-05,
                            "NFLX": 1.063194103889454e-05,
                            "CVX": 1.856142655999487e-05,
                            "PFE": 7.37712367461191e-05,
                            "MMM": 4.6508322752181456e-05,
                            "MSFT": 1.1064277909064516e-05
                        },
                        "annual_variance": {
                            "CSCO": 0.005839454771186103,
                            "NFLX": 0.0026792491418014238,
                            "CVX": 0.004677479493118707,
                            "PFE": 0.01859035166002201,
                            "MMM": 0.011720097333549728,
                            "MSFT": 0.002788198033084258
                        },
                        "daily_standard_deviation": {
                            "CSCO": 0.0017096443673059118,
                            "NFLX": 0.000784416248327171,
                            "CVX": 0.0013694474539058725,
                            "PFE": 0.0054427838295144524,
                            "MMM": 0.003431347476043623,
                            "MSFT": 0.0008163137225956613
                        },
                        "annual_standard_deviation": {
                            "CSCO": 0.02713976295752285,
                            "NFLX": 0.012452221904591883,
                            "CVX": 0.021739304379633166,
                            "PFE": 0.0864015147166741,
                            "MMM": 0.05447095250076354,
                            "MSFT": 0.012958578610784924
                        },
                        "daily_semi_variance": {
                            "CSCO": 1.1670626835411515e-05,
                            "NFLX": 5.354698025464756e-06,
                            "CVX": 9.348324429849152e-06,
                            "PFE": 3.7154334687846384e-05,
                            "MMM": 2.3423570832243578e-05,
                            "MSFT": 5.572441274469407e-06
                        },
                        "annual_semi_variance": {
                            "CSCO": 0.0029409979625237017,
                            "NFLX": 0.0013493839024171183,
                            "CVX": 0.0023557777563219862,
                            "PFE": 0.00936289234133729,
                            "MMM": 0.005902739849725381,
                            "MSFT": 0.0014042552011662903
                        },
                        "daily_semi_deviation": {
                            "CSCO": 0.0012132966320977069,
                            "NFLX": 0.0005566827876360203,
                            "CVX": 0.0009718664392624933,
                            "PFE": 0.0038626227862768856,
                            "MMM": 0.002435151085135446,
                            "MSFT": 0.0005793197166035156
                        },
                        "annual_semi_deviation": {
                            "CSCO": 0.01926048693049656,
                            "NFLX": 0.00883706529141055,
                            "CVX": 0.015427901435150502,
                            "PFE": 0.06131723580564019,
                            "MMM": 0.0386568250568248,
                            "MSFT": 0.009196415398375912
                        },
                        "mean_absolute_deviation": {
                            "CSCO": 0.0011734811760043841,
                            "NFLX": 0.0005384147248204915,
                            "CVX": 0.0009399737392274425,
                            "PFE": 0.0037358672313008703,
                            "MMM": 0.002355239340104731,
                            "MSFT": 0.0005603088019349864
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "CSCO": -0.002248485672341024,
                            "NFLX": -0.0010316465396218572,
                            "CVX": -0.001801066372641862,
                            "PFE": -0.007158226407985394,
                            "MMM": -0.004512830729156606,
                            "MSFT": -0.001073597377613729
                        },
                        "kurtosis": {
                            "CSCO": 1.5102344422128673,
                            "NFLX": 0.6929233107829857,
                            "CVX": 1.2097175010428938,
                            "PFE": 4.807947054980216,
                            "MMM": 3.031121115374058,
                            "MSFT": 0.7211003195112886
                        },
                        "first_lower_partial_moment": {
                            "CSCO": 0.0005867405880021921,
                            "NFLX": 0.00026920736241024573,
                            "CVX": 0.00046998686961372124,
                            "PFE": 0.0018679336156504352,
                            "MMM": 0.0011776196700523656,
                            "MSFT": 0.0002801544009674932
                        },
                        "fourth_central_moment": {
                            "CSCO": 5.096925484459122e-08,
                            "NFLX": 2.338563061990997e-08,
                            "CVX": 4.0827038423433436e-08,
                            "PFE": 1.6226452786066685e-07,
                            "MMM": 1.0229801431885636e-07,
                            "MSFT": 2.433658306708553e-08
                        },
                        "fourth_lower_partial_moment": {
                            "CSCO": 2.579207810332919e-08,
                            "NFLX": 1.183387933144036e-08,
                            "CVX": 2.065979122032547e-08,
                            "PFE": 8.211105672906017e-08,
                            "MMM": 5.176607708259291e-08,
                            "MSFT": 1.2315091777352876e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "CSCO": 0.0024478581471287647,
                            "NFLX": 0.0011231222942778658,
                            "CVX": 0.00196076632732146,
                            "PFE": 0.007792943956603401,
                            "MMM": 0.004912981925064985,
                            "MSFT": 0.0011687928990855747
                        },
                        "conditional_var_at_95": {
                            "CSCO": 0.0038211441466704937,
                            "NFLX": 0.0017532111433045596,
                            "CVX": 0.003060786338220307,
                            "PFE": 0.012164905151891496,
                            "MMM": 0.007669240208089751,
                            "MSFT": 0.0018245036585348953
                        },
                        "entropic_var_at_95": {
                            "CSCO": 0.007115874206791744,
                            "NFLX": 0.0032648938314905666,
                            "CVX": 0.005699908121922151,
                            "PFE": 0.022653930727486192,
                            "MMM": 0.014281939253714836,
                            "MSFT": 0.0033976573574902046
                        },
                        "drawdown_at_risk_at_95": {
                            "CSCO": 0.036695036320181486,
                            "NFLX": 0.016836356889745833,
                            "CVX": 0.02939320306646226,
                            "PFE": 0.11682145955398703,
                            "MMM": 0.07364889603268804,
                            "MSFT": 0.017520989904183076
                        },
                        "conditional_dar_at_95": {
                            "CSCO": 0.038790683467569254,
                            "NFLX": 0.017797878305899694,
                            "CVX": 0.03107184378564159,
                            "PFE": 0.12349311280789986,
                            "MMM": 0.07785497168642097,
                            "MSFT": 0.01852161059281603
                        },
                        "entropic_dar_at_95": {
                            "CSCO": 0.03973468692876967,
                            "NFLX": 0.018231004438798066,
                            "CVX": 0.03182800287997792,
                            "PFE": 0.12649842015244653,
                            "MMM": 0.07974963700741453,
                            "MSFT": 0.018972349351292467
                        },
                        "entropic_risk_measure_at_95": {
                            "CSCO": 0.37784372074530326,
                            "NFLX": 0.1733616414904239,
                            "CVX": 0.302657752246079,
                            "PFE": 1.2028944338855776,
                            "MMM": 0.7583525102132185,
                            "MSFT": 0.18041121307996805
                        },
                        "worst_realization": {
                            "CSCO": 0.012035243272962204,
                            "NFLX": 0.00552199074639047,
                            "CVX": 0.009640386955602891,
                            "PFE": 0.03831511905225973,
                            "MMM": 0.024155375479244588,
                            "MSFT": 0.005746536780615869
                        },
                        "average_drawdown": {
                            "CSCO": 0.014175791358552755,
                            "NFLX": 0.0065041135379911436,
                            "CVX": 0.011354993912366872,
                            "PFE": 0.04512971788307359,
                            "MMM": 0.028451569711975853,
                            "MSFT": 0.006768596578290024
                        },
                        "max_drawdown": {
                            "CSCO": 0.043283164318346626,
                            "NFLX": 0.019859111064032653,
                            "CVX": 0.03467037958669402,
                            "PFE": 0.13779526979248122,
                            "MMM": 0.08687162048384361,
                            "MSFT": 0.02066666124610877
                        },
                        "ulcer_index": {
                            "CSCO": 0.018981308614997142,
                            "NFLX": 0.008708973150702104,
                            "CVX": 0.015204275960368942,
                            "PFE": 0.06042845024870839,
                            "MMM": 0.038096499279970636,
                            "MSFT": 0.009063114523438722
                        },
                        "gini_mean_difference": {
                            "CSCO": 0.0017349750007414671,
                            "NFLX": 0.00079603840836656,
                            "CVX": 0.0013897376219241533,
                            "PFE": 0.005523425841789587,
                            "MMM": 0.003482187409054163,
                            "MSFT": 0.0008284084857352426
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "CSCO": 0.0028178412795891775,
                            "NFLX": 0.0012928773534345644,
                            "CVX": 0.0022571276457484346,
                            "PFE": 0.008970813605436815,
                            "MMM": 0.005655557815129955,
                            "MSFT": 0.001345450871896783
                        },
                        "annual_sharpe_ratio": {
                            "CSCO": 0.044731843559069936,
                            "NFLX": 0.0205237917173713,
                            "CVX": 0.035830790567874325,
                            "PFE": 0.1424072511474031,
                            "MMM": 0.08977919702509002,
                            "MSFT": 0.02135837044976346
                        },
                        "daily_sortino_ratio": {
                            "CSCO": 0.003970592470270507,
                            "NFLX": 0.0018217807801009188,
                            "CVX": 0.003180496396147178,
                            "PFE": 0.012640685340212177,
                            "MMM": 0.007969190968487921,
                            "MSFT": 0.00189586160858965
                        },
                        "annual_sortino_ratio": {
                            "CSCO": 0.06303120140352832,
                            "NFLX": 0.02891987332454567,
                            "CVX": 0.05048881505965561,
                            "PFE": 0.2006646588697279,
                            "MMM": 0.12650698471800606,
                            "MSFT": 0.03009587001913854
                        },
                        "mean_absolute_deviation_ratio": {
                            "CSCO": 0.0041053121005442715,
                            "NFLX": 0.0018835926217776158,
                            "CVX": 0.0032884085784686233,
                            "PFE": 0.013069575604874458,
                            "MMM": 0.00823958045542073,
                            "MSFT": 0.0019601869647856793
                        },
                        "calmar_ratio": {
                            "CSCO": 0.00011130208586828533,
                            "NFLX": 5.106744203495913e-05,
                            "CVX": 8.915442358747745e-05,
                            "PFE": 0.00035433871788771617,
                            "MMM": 0.00022338922569280402,
                            "MSFT": 5.314404667151725e-05
                        },
                        "value_at_risk_ratio_at_95": {
                            "CSCO": 0.0019680496916303965,
                            "NFLX": 0.0009029773590064596,
                            "CVX": 0.0015764334916100332,
                            "PFE": 0.00626543697749636,
                            "MMM": 0.003949980751111408,
                            "MSFT": 0.0009396959980394499
                        },
                        "conditional_var_ratio_at_95": {
                            "CSCO": 0.0012607497353402366,
                            "NFLX": 0.0005784551432959543,
                            "CVX": 0.0010098769943569536,
                            "PFE": 0.004013693376118748,
                            "MMM": 0.0025303919955584017,
                            "MSFT": 0.0006019774225553492
                        },
                        "entropic_var_ratio_at_95": {
                            "CSCO": 0.0006770083803636737,
                            "NFLX": 0.00031062388410507593,
                            "CVX": 0.0005422925495452341,
                            "PFE": 0.0021553080485947865,
                            "MMM": 0.0013587919462349812,
                            "MSFT": 0.00032325508261932137
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "CSCO": 0.00013128496261937734,
                            "NFLX": 6.02359530490811e-05,
                            "CVX": 0.00010516096869815496,
                            "PFE": 0.00041795573703387563,
                            "MMM": 0.0002634959256680751,
                            "MSFT": 6.268538568961925e-05
                        },
                        "conditional_dar_ratio_at_95": {
                            "CSCO": 0.00012419235860175988,
                            "NFLX": 5.698173600794473e-05,
                            "CVX": 9.94797003015032e-05,
                            "PFE": 0.0003953758887364957,
                            "MMM": 0.000249260690925788,
                            "MSFT": 5.9298839283104366e-05
                        },
                        "entropic_dar_ratio_at_95": {
                            "CSCO": 0.00012124183789966221,
                            "NFLX": 5.562798289764248e-05,
                            "CVX": 9.71162947064838e-05,
                            "PFE": 0.00038598268002413004,
                            "MMM": 0.00024333883842958073,
                            "MSFT": 5.789003720473976e-05
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "CSCO": 1.2749997438383005e-05,
                            "NFLX": 5.849933090212015e-06,
                            "CVX": 1.0212914371668123e-05,
                            "PFE": 4.059059369951679e-05,
                            "MMM": 2.5589925230297866e-05,
                            "MSFT": 6.0878145601782e-06
                        },
                        "worst_realization_ratio": {
                            "CSCO": 0.0004002832649369454,
                            "NFLX": 0.00018365731666450537,
                            "CVX": 0.00032063212004309466,
                            "PFE": 0.0012743324420488806,
                            "MMM": 0.0008033898728355369,
                            "MSFT": 0.00019112555122111877
                        },
                        "average_drawdown_ratio": {
                            "CSCO": 0.00033984039054759,
                            "NFLX": 0.00015592501533137965,
                            "CVX": 0.0002722165887067788,
                            "PFE": 0.0010819079205361605,
                            "MMM": 0.0006820777985545203,
                            "MSFT": 0.00016226554457838752
                        },
                        "ulcer_index_ratio": {
                            "CSCO": 0.0002538026523527153,
                            "NFLX": 0.00011644932021021831,
                            "CVX": 0.00020329923737688756,
                            "PFE": 0.0008080001891212387,
                            "MMM": 0.0005093954668104589,
                            "MSFT": 0.00012118461120260908
                        },
                        "gini_mean_difference_ratio": {
                            "CSCO": 0.0027767007994656335,
                            "NFLX": 0.0012740013452482875,
                            "CVX": 0.002224173584169866,
                            "PFE": 0.008839839734942484,
                            "MMM": 0.00557298667616402,
                            "MSFT": 0.0013258072903886919
                        }
                    }
                },
                "allocation": {
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.4015643092231909,
                        "Shares": 14114,
                        "Purchase Value": 401579.3301542756,
                        "Current Value": 403378.1189231018,
                        "Net Value": 1798.7887688262272,
                        "Net Change": 0.004479286242484599,
                        "%Shares": 0.6880514795495539,
                        "%Purchase Value": 0.40158397312588945,
                        "%Current Value": 0.34053668579681307
                    },
                    "MMM": {
                        "Company Name": "3M Company",
                        "Sector": "Industrials",
                        "Industry": "Conglomerates",
                        "Market Cap": 74311114752,
                        "Volume (3 Months Average)": 4169252.3076923075,
                        "Current Price": 135.2700042725,
                        "Purchase Price": 89.3647994995,
                        "Price Diff": 45.905204772999994,
                        "Weight": 0.2531621174168733,
                        "Shares": 2834,
                        "Purchase Value": 253259.84178158297,
                        "Current Value": 383355.19210826495,
                        "Net Value": 130095.35032668198,
                        "Net Change": 0.5136832962206427,
                        "%Shares": 0.1381562911324526,
                        "%Purchase Value": 0.2532627699159964,
                        "%Current Value": 0.3236330888548665
                    },
                    "CSCO": {
                        "Company Name": "Cisco Systems, Inc.",
                        "Sector": "Technology",
                        "Industry": "Communication Equipment",
                        "Market Cap": 210511003648,
                        "Volume (3 Months Average)": 18805300.0,
                        "Current Price": 52.75,
                        "Purchase Price": 48.9177017212,
                        "Price Diff": 3.8322982788000033,
                        "Weight": 0.12613621648019097,
                        "Shares": 2580,
                        "Purchase Value": 126207.67044069599,
                        "Current Value": 136095.0,
                        "Net Value": 9887.32955930401,
                        "Net Change": 0.07834174836425643,
                        "%Shares": 0.12577389947837955,
                        "%Purchase Value": 0.12620912962593614,
                        "%Current Value": 0.11489304471260212
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.101036755834969,
                        "Shares": 699,
                        "Purchase Value": 101192.87841793381,
                        "Current Value": 105367.2638397468,
                        "Net Value": 4174.385421812985,
                        "Net Change": 0.04125177074786306,
                        "%Shares": 0.03407595183542144,
                        "%Purchase Value": 0.10119404838766767,
                        "%Current Value": 0.0889523182746212
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.060226984277048035,
                        "Shares": 163,
                        "Purchase Value": 60123.217559817,
                        "Current Value": 67817.7796020518,
                        "Net Value": 7694.5620422348,
                        "Net Change": 0.1279798778995723,
                        "%Shares": 0.00794618047092088,
                        "%Purchase Value": 0.060123912691193306,
                        "%Current Value": 0.057252589618486595
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.057873613718560604,
                        "Shares": 123,
                        "Purchase Value": 57625.5,
                        "Current Value": 88523.101501461,
                        "Net Value": 30897.601501461002,
                        "Net Change": 0.5361793216798293,
                        "%Shares": 0.005996197533271584,
                        "%Purchase Value": 0.05762616625331696,
                        "%Current Value": 0.07473227274261049
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 11.561645694542712
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.07630328664819717,
                    "Expected Daily Return": 0.0003027908200325285,
                    "Expected Current Return": 0.05783304662621294,
                    "Net Value": 184548.0176203209,
                    "Net Change": 0.18455015132378338,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.02351963411278474,
                        "95.0% CVaR": 0.030293790646711498,
                        "99.0% CVaR": 0.054679874226695714,
                        "99.9% CVaR": 0.0946207973035179
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.04687640078099363,
                        "95.0% EVaR": 0.056414203498895685,
                        "99.0% EVaR": 0.07589544636228354,
                        "99.9% EVaR": 0.09526256965930749
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.2915921020474239,
                        "95.0% CDaR": 0.30753010064624736,
                        "99.0% CDaR": 0.32598525644299464,
                        "99.9% CDaR": 0.3428110006327163
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.30214213916087385,
                        "95.0% EDaR": 0.3150141007586991,
                        "99.0% EDaR": 0.3321360139363337,
                        "99.9% EDaR": 0.3436930141097595
                    },
                    "VaR": {
                        "90.0% VaR": 0.013924686533960975,
                        "95.0% VaR": 0.019406465549482048,
                        "99.0% VaR": 0.034538889336435084,
                        "99.9% VaR": 0.08311565261427391
                    },
                    "DaR": {
                        "90.0% DaR": 0.25904099815877674,
                        "95.0% DaR": 0.29091594176724767,
                        "99.0% DaR": 0.31947106261601704,
                        "99.9% DaR": 0.3379529447082154
                    },
                    "ERM": {
                        "90.0% ERM": 2.302374091100625,
                        "95.0% ERM": 2.9955212716605697,
                        "99.0% ERM": 4.60495918409467,
                        "99.9% ERM": 6.907544277088715
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "CSCO": 0.002966677669030997,
                            "NFLX": 0.0013611662235956086,
                            "CVX": 0.002376347536427121,
                            "PFE": 0.009444645654480907,
                            "MMM": 0.0059542803910183064,
                            "MSFT": 0.0014165166382318056
                        },
                        "95.0% CVaR": {
                            "CSCO": 0.0038211441466704937,
                            "NFLX": 0.0017532111433045596,
                            "CVX": 0.003060786338220307,
                            "PFE": 0.012164905151891496,
                            "MMM": 0.007669240208089751,
                            "MSFT": 0.0018245036585348953
                        },
                        "99.0% CVaR": {
                            "CSCO": 0.006897112473598555,
                            "NFLX": 0.0031645219288244223,
                            "CVX": 0.005524677118175134,
                            "PFE": 0.021957485989206074,
                            "MMM": 0.01384287278152784,
                            "MSFT": 0.003293203935363697
                        },
                        "99.9% CVaR": {
                            "CSCO": 0.011935109408596949,
                            "NFLX": 0.005476047489583401,
                            "CVX": 0.009560178423216215,
                            "PFE": 0.037996335223191915,
                            "MMM": 0.023954401470072346,
                            "MSFT": 0.005698725288857088
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "CSCO": 0.005912811854752758,
                            "NFLX": 0.0027129067195877645,
                            "CVX": 0.004736239474572991,
                            "PFE": 0.018823889555886344,
                            "MMM": 0.011867328914783792,
                            "MSFT": 0.0028232242614099888
                        },
                        "95.0% EVaR": {
                            "CSCO": 0.007115874206791744,
                            "NFLX": 0.0032648938314905666,
                            "CVX": 0.005699908121922151,
                            "PFE": 0.022653930727486192,
                            "MMM": 0.014281939253714836,
                            "MSFT": 0.0033976573574902046
                        },
                        "99.0% EVaR": {
                            "CSCO": 0.009573164481403898,
                            "NFLX": 0.004392343759161524,
                            "CVX": 0.0076682297064737445,
                            "PFE": 0.030476902584585304,
                            "MMM": 0.019213851961960685,
                            "MSFT": 0.004570953868698397
                        },
                        "99.9% EVaR": {
                            "CSCO": 0.012016060145644658,
                            "NFLX": 0.005513189175110869,
                            "CVX": 0.009625021020227477,
                            "PFE": 0.03825404809670891,
                            "MMM": 0.02411687391905906,
                            "MSFT": 0.005737377302556529
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "CSCO": 0.03678032461991716,
                            "NFLX": 0.016875488728731906,
                            "CVX": 0.02946152010780404,
                            "PFE": 0.11709298139064807,
                            "MMM": 0.07382007420145259,
                            "MSFT": 0.017561712998870188
                        },
                        "95.0% CDaR": {
                            "CSCO": 0.038790683467569254,
                            "NFLX": 0.017797878305899694,
                            "CVX": 0.03107184378564159,
                            "PFE": 0.12349311280789986,
                            "MMM": 0.07785497168642097,
                            "MSFT": 0.01852161059281603
                        },
                        "99.0% CDaR": {
                            "CSCO": 0.041118547001421465,
                            "NFLX": 0.018865944866853213,
                            "CVX": 0.032936492861459485,
                            "PFE": 0.13090404471962422,
                            "MMM": 0.08252711801942995,
                            "MSFT": 0.019633108974206344
                        },
                        "99.9% CDaR": {
                            "CSCO": 0.04324088271944787,
                            "NFLX": 0.01983971148958566,
                            "CVX": 0.03463651147408168,
                            "PFE": 0.13766066308293798,
                            "MMM": 0.0867867590586029,
                            "MSFT": 0.02064647280806026
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "CSCO": 0.038111066389190984,
                            "NFLX": 0.01748605750321391,
                            "CVX": 0.030527461634935776,
                            "PFE": 0.12132949976930747,
                            "MMM": 0.07649094394406411,
                            "MSFT": 0.01819710992016164
                        },
                        "95.0% EDaR": {
                            "CSCO": 0.03973468692876967,
                            "NFLX": 0.018231004438798066,
                            "CVX": 0.03182800287997792,
                            "PFE": 0.12649842015244653,
                            "MMM": 0.07974963700741453,
                            "MSFT": 0.018972349351292467
                        },
                        "99.0% EDaR": {
                            "CSCO": 0.04189438028248409,
                            "NFLX": 0.019221911431184662,
                            "CVX": 0.033557945446409,
                            "PFE": 0.1333739694111675,
                            "MMM": 0.08408425681490934,
                            "MSFT": 0.02000355055017915
                        },
                        "99.9% EDaR": {
                            "CSCO": 0.04335213656266587,
                            "NFLX": 0.019890756797006266,
                            "CVX": 0.03472562725467657,
                            "PFE": 0.13801484821665236,
                            "MMM": 0.08701005145872223,
                            "MSFT": 0.02069959382003626
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "CSCO": 0.0017564072804220811,
                            "NFLX": 0.0008058719320757384,
                            "CVX": 0.0014069051577001851,
                            "PFE": 0.005591657146209406,
                            "MMM": 0.003525203138052717,
                            "MSFT": 0.0008386418795008496
                        },
                        "95.0% VaR": {
                            "CSCO": 0.0024478581471287647,
                            "NFLX": 0.0011231222942778658,
                            "CVX": 0.00196076632732146,
                            "PFE": 0.007792943956603401,
                            "MMM": 0.004912981925064985,
                            "MSFT": 0.0011687928990855747
                        },
                        "99.0% VaR": {
                            "CSCO": 0.004356604835609952,
                            "NFLX": 0.001998890345819907,
                            "CVX": 0.0034896973393370775,
                            "PFE": 0.013869585280012475,
                            "MMM": 0.008743938384300704,
                            "MSFT": 0.002080173151354974
                        },
                        "99.9% VaR": {
                            "CSCO": 0.01048389398301355,
                            "NFLX": 0.004810203188031674,
                            "CVX": 0.008397735924858598,
                            "PFE": 0.03337627972945546,
                            "MMM": 0.021041734670474634,
                            "MSFT": 0.005005805118439999
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "CSCO": 0.03267445152063008,
                            "NFLX": 0.014991638710423428,
                            "CVX": 0.026172662162019807,
                            "PFE": 0.10402161980329437,
                            "MMM": 0.06557936779161876,
                            "MSFT": 0.015601258170790323
                        },
                        "95.0% DaR": {
                            "CSCO": 0.036695036320181486,
                            "NFLX": 0.016836356889745833,
                            "CVX": 0.02939320306646226,
                            "PFE": 0.11682145955398703,
                            "MMM": 0.07364889603268804,
                            "MSFT": 0.017520989904183076
                        },
                        "99.0% DaR": {
                            "CSCO": 0.04029687123616247,
                            "NFLX": 0.018488944928473344,
                            "CVX": 0.03227831984829461,
                            "PFE": 0.12828817696737177,
                            "MMM": 0.08087797091189985,
                            "MSFT": 0.019240778723815043
                        },
                        "99.9% DaR": {
                            "CSCO": 0.04262810592381369,
                            "NFLX": 0.019558558236730646,
                            "CVX": 0.0341456692623086,
                            "PFE": 0.13570984120549978,
                            "MMM": 0.08555688333047658,
                            "MSFT": 0.02035388674938618
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "CSCO": 0.29041275765896846,
                            "NFLX": 0.13324670919027115,
                            "CVX": 0.2326244095926033,
                            "PFE": 0.9245512642853061,
                            "MMM": 0.5828739017660635,
                            "MSFT": 0.13866504860741305
                        },
                        "95.0% ERM": {
                            "CSCO": 0.37784372074530326,
                            "NFLX": 0.1733616414904239,
                            "CVX": 0.302657752246079,
                            "PFE": 1.2028944338855776,
                            "MMM": 0.7583525102132185,
                            "MSFT": 0.18041121307996805
                        },
                        "99.0% ERM": {
                            "CSCO": 0.5808521302985242,
                            "NFLX": 0.26650562982265324,
                            "CVX": 0.4652701381320578,
                            "PFE": 1.8491872594004464,
                            "MMM": 1.165801221218407,
                            "MSFT": 0.2773428052225823
                        },
                        "99.9% ERM": {
                            "CSCO": 0.87129150293808,
                            "NFLX": 0.3997645504550353,
                            "CVX": 0.6979158666715123,
                            "PFE": 2.773823254515587,
                            "MMM": 1.7487285406707505,
                            "MSFT": 0.4160205618377515
                        }
                    }
                }
            }
        },
        {
            "name": "CVaR 99%",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.07265192031871683,
                    "annual_standard_deviation": 0.22270464275262747,
                    "annual_sharpe_ratio": 0.32622544110773677,
                    "annual_sortino_ratio": 0.4617612246642673,
                    "cvar_900": -0.024262947901168824,
                    "cvar_950": -0.03155664286696439,
                    "cvar_990": -0.05335872658843755,
                    "cvar_999": -0.09299813810018669,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.16202343518248352
                        }
                    ]
                },
                "weights": [
                    1.430244497485268e-09,
                    0.009689311830163534,
                    0.09428293106635388,
                    7.553107977775311e-11,
                    0.15491246193941888,
                    0.5297069024670922,
                    0.21140839088487615,
                    3.0631959161989314e-10
                ],
                "position": [
                    0.22270464275262747,
                    0.07265192031871683
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.0002883012711060192,
                        "annual_mean_return": 0.07265192031871683,
                        "daily_variance": 0.00019681491231577546,
                        "annual_variance": 0.04959735790357542,
                        "daily_standard_deviation": 0.014029073822450841,
                        "annual_standard_deviation": 0.22270464275262747,
                        "daily_semi_variance": 9.823329975213135e-05,
                        "annual_semi_variance": 0.0247547915375371,
                        "daily_semi_deviation": 0.009911271348930537,
                        "annual_semi_deviation": 0.15733655499449928,
                        "mean_absolute_deviation": 0.00978105697122337
                    },
                    "stats_moments": {
                        "skew": -0.00770912260202206,
                        "kurtosis": 9.742330474008913,
                        "first_lower_partial_moment": 0.004890528485611686,
                        "fourth_central_moment": 3.7737998207098385e-07,
                        "fourth_lower_partial_moment": 1.94949766566287e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.01931216166034006,
                        "conditional_var_at_95": 0.03155664286696439,
                        "entropic_var_at_95": 0.05548377227288516,
                        "drawdown_at_risk_at_95": 0.31903088041861377,
                        "conditional_dar_at_95": 0.3450998502923125,
                        "entropic_dar_at_95": 0.3527381685811961,
                        "entropic_risk_measure_at_95": 2.9955423021404934,
                        "worst_realization": 0.09403341482746683,
                        "average_drawdown": 0.11434367807964985,
                        "max_drawdown": 0.3818107163744202,
                        "ulcer_index": 0.15386725546910734,
                        "gini_mean_difference": 0.014472271852531408
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.020550271155081408,
                        "annual_sharpe_ratio": 0.32622544110773677,
                        "daily_sortino_ratio": 0.029088222989387527,
                        "annual_sortino_ratio": 0.4617612246642673,
                        "mean_absolute_deviation_ratio": 0.029475472022525165,
                        "calmar_ratio": 0.0007550895214352716,
                        "value_at_risk_ratio_at_95": 0.0149284826927522,
                        "conditional_var_ratio_at_95": 0.009135993087776528,
                        "entropic_var_ratio_at_95": 0.005196136803533663,
                        "drawdown_at_risk_ratio_at_95": 0.0009036782606364845,
                        "conditional_dar_ratio_at_95": 0.0008354140717876788,
                        "entropic_dar_ratio_at_95": 0.0008173237170948674,
                        "entropic_risk_measure_ratio_at_95": 9.624343174857212e-05,
                        "worst_realization_ratio": 0.0030659449264391425,
                        "average_drawdown_ratio": 0.002521357332105352,
                        "ulcer_index_ratio": 0.0018737012642946814,
                        "gini_mean_difference_ratio": 0.019920940820054533
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "CSCO": 2.7934409218407174e-06,
                            "NFLX": 2.7181888919287184e-05,
                            "CVX": 4.46614597682281e-05,
                            "PFE": 0.00015271517357162926,
                            "MMM": 6.094930792503391e-05
                        },
                        "annual_mean_return": {
                            "CSCO": 0.0007039471123038607,
                            "NFLX": 0.0068498360076603695,
                            "CVX": 0.01125468786159348,
                            "PFE": 0.03848422374005057,
                            "MMM": 0.015359225597108544
                        },
                        "daily_variance": {
                            "CSCO": 1.9070010617095096e-06,
                            "NFLX": 1.8556286844324504e-05,
                            "CVX": 3.0489082668476752e-05,
                            "PFE": 0.00010425421775104035,
                            "MMM": 4.160832399022434e-05
                        },
                        "annual_variance": {
                            "CSCO": 0.0004805642675507964,
                            "NFLX": 0.004676184284769775,
                            "CVX": 0.007683248832456142,
                            "PFE": 0.02627206287326217,
                            "MMM": 0.010485297645536533
                        },
                        "daily_standard_deviation": {
                            "CSCO": 0.00013593207120043236,
                            "NFLX": 0.001322702202523785,
                            "CVX": 0.0021732783685039013,
                            "PFE": 0.007431297252438823,
                            "MMM": 0.002965863927783899
                        },
                        "annual_standard_deviation": {
                            "CSCO": 0.0021578547335656152,
                            "NFLX": 0.02099724651885196,
                            "CVX": 0.03449972455666507,
                            "PFE": 0.11796818669130424,
                            "MMM": 0.047081630252240575
                        },
                        "daily_semi_variance": {
                            "CSCO": 9.518130751291029e-07,
                            "NFLX": 9.261723445733805e-06,
                            "CVX": 1.5217562336611246e-05,
                            "PFE": 5.2034857025114996e-05,
                            "MMM": 2.07673438695422e-05
                        },
                        "annual_semi_variance": {
                            "CSCO": 0.00023985689493253394,
                            "NFLX": 0.0023339543083249186,
                            "CVX": 0.003834825708826034,
                            "PFE": 0.013112783970328978,
                            "MMM": 0.0052333706551246344
                        },
                        "daily_semi_deviation": {
                            "CSCO": 9.603339890717522e-05,
                            "NFLX": 0.0009344637150644834,
                            "CVX": 0.0015353794483947084,
                            "PFE": 0.005250068855266458,
                            "MMM": 0.002095325931297711
                        },
                        "annual_semi_deviation": {
                            "CSCO": 0.0015244829463878858,
                            "NFLX": 0.01483415159564487,
                            "CVX": 0.024373393131431567,
                            "PFE": 0.08334225934200364,
                            "MMM": 0.03326226797903132
                        },
                        "mean_absolute_deviation": {
                            "CSCO": 9.477171119451348e-05,
                            "NFLX": 0.0009221867218450235,
                            "CVX": 0.0015152076185276286,
                            "PFE": 0.005181093400469525,
                            "MMM": 0.0020677975191866795
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "CSCO": -7.469609296330988e-05,
                            "NFLX": -0.0007268386761856176,
                            "CVX": -0.0011942391638361314,
                            "PFE": -0.004083575461655983,
                            "MMM": -0.0016297732073810177
                        },
                        "kurtosis": {
                            "CSCO": 0.0943964780862327,
                            "NFLX": 0.918535474171095,
                            "CVX": 1.509208401490976,
                            "PFE": 5.1605797075494815,
                            "MMM": 2.0596104127111277
                        },
                        "first_lower_partial_moment": {
                            "CSCO": 4.7385855597256755e-05,
                            "NFLX": 0.0004610933609225118,
                            "CVX": 0.0007576038092638145,
                            "PFE": 0.002590546700234763,
                            "MMM": 0.00103389875959334
                        },
                        "fourth_central_moment": {
                            "CSCO": 3.6565523313733076e-09,
                            "NFLX": 3.558049089989568e-08,
                            "CVX": 5.846086221520652e-08,
                            "PFE": 1.9990078171814692e-07,
                            "MMM": 7.978129490636142e-08
                        },
                        "fourth_lower_partial_moment": {
                            "CSCO": 1.8889290829012637e-09,
                            "NFLX": 1.838043543587812e-08,
                            "CVX": 3.020014834802408e-08,
                            "PFE": 1.0326623717163884e-07,
                            "MMM": 4.1214016527844694e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "CSCO": 0.0001871215567806457,
                            "NFLX": 0.0018208072098636007,
                            "CVX": 0.00299169451359657,
                            "PFE": 0.010229785351579816,
                            "MMM": 0.004082753028519429
                        },
                        "conditional_var_at_95": {
                            "CSCO": 0.00030576215360519394,
                            "NFLX": 0.0029752527895029936,
                            "CVX": 0.004888517245922915,
                            "PFE": 0.01671577157561054,
                            "MMM": 0.006671339102322749
                        },
                        "entropic_var_at_95": {
                            "CSCO": 0.0005375995720399474,
                            "NFLX": 0.005231172685985093,
                            "CVX": 0.008595127776053898,
                            "PFE": 0.029390137201117262,
                            "MMM": 0.011729735037688958
                        },
                        "drawdown_at_risk_at_95": {
                            "CSCO": 0.0030911896894290926,
                            "NFLX": 0.03007916656105267,
                            "CVX": 0.04942185920990492,
                            "PFE": 0.16899285976412437,
                            "MMM": 0.06744580519410272
                        },
                        "conditional_dar_at_95": {
                            "CSCO": 0.0033437800680842164,
                            "NFLX": 0.03253702545507934,
                            "CVX": 0.05346026752058211,
                            "PFE": 0.18280177307145232,
                            "MMM": 0.0729570041771145
                        },
                        "entropic_dar_at_95": {
                            "CSCO": 0.003417790115977364,
                            "NFLX": 0.03325718849307802,
                            "CVX": 0.05464353821393416,
                            "PFE": 0.18684784299964646,
                            "MMM": 0.07457180875856008
                        },
                        "entropic_risk_measure_at_95": {
                            "CSCO": 0.02902474351848079,
                            "NFLX": 0.2824285088908466,
                            "CVX": 0.4640468337091555,
                            "PFE": 1.5867594369513425,
                            "MMM": 0.633282779070668
                        },
                        "worst_realization": {
                            "CSCO": 0.000911119080369484,
                            "NFLX": 0.00886574598417749,
                            "CVX": 0.014566947821890238,
                            "PFE": 0.04981014898692133,
                            "MMM": 0.01987945295410828
                        },
                        "average_drawdown": {
                            "CSCO": 0.0011079115547292034,
                            "NFLX": 0.010780657137792565,
                            "CVX": 0.01771326071062504,
                            "PFE": 0.060568635642021806,
                            "MMM": 0.024173213034481226
                        },
                        "max_drawdown": {
                            "CSCO": 0.0036994830977536996,
                            "NFLX": 0.03599823351755689,
                            "CVX": 0.05914723817559506,
                            "PFE": 0.20224777226592786,
                            "MMM": 0.08071798931758671
                        },
                        "ulcer_index": {
                            "CSCO": 0.0014908678213932111,
                            "NFLX": 0.01450705586705108,
                            "CVX": 0.023835955399773956,
                            "PFE": 0.0815045474333476,
                            "MMM": 0.032528828947541485
                        },
                        "gini_mean_difference": {
                            "CSCO": 0.00014022635512417884,
                            "NFLX": 0.0013644882119183352,
                            "CVX": 0.0022419352665947953,
                            "PFE": 0.007666062308557734,
                            "MMM": 0.0030595597103363647
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "CSCO": 0.0001991179857768195,
                            "NFLX": 0.001937539802220428,
                            "CVX": 0.003183493103925079,
                            "PFE": 0.010885620498142788,
                            "MMM": 0.004344499765016293
                        },
                        "annual_sharpe_ratio": {
                            "CSCO": 0.0031609000315533636,
                            "NFLX": 0.03075749083178714,
                            "CVX": 0.050536386320849155,
                            "PFE": 0.17280386822827712,
                            "MMM": 0.06896679569526996
                        },
                        "daily_sortino_ratio": {
                            "CSCO": 0.00028184486364023724,
                            "NFLX": 0.0027425229279208676,
                            "CVX": 0.004506128244894358,
                            "PFE": 0.015408232525901714,
                            "MMM": 0.00614949442703035
                        },
                        "annual_sortino_ratio": {
                            "CSCO": 0.0044741485049578705,
                            "NFLX": 0.04353620179302801,
                            "CVX": 0.07153256827052658,
                            "PFE": 0.24459810843955515,
                            "MMM": 0.09762019765619964
                        },
                        "mean_absolute_deviation_ratio": {
                            "CSCO": 0.00028559704028503644,
                            "NFLX": 0.0027790339018838573,
                            "CVX": 0.004566117946110076,
                            "PFE": 0.01561336101210014,
                            "MMM": 0.0062313621221460535
                        },
                        "calmar_ratio": {
                            "CSCO": 7.316297846133128e-06,
                            "NFLX": 7.119205342741465e-05,
                            "CVX": 0.00011697277696216135,
                            "PFE": 0.0003999761322096316,
                            "MMM": 0.00015963226098993086
                        },
                        "value_at_risk_ratio_at_95": {
                            "CSCO": 0.00014464672422338911,
                            "NFLX": 0.0014075011071965388,
                            "CVX": 0.0023126080111449147,
                            "PFE": 0.007907720340040905,
                            "MMM": 0.00315600651014645
                        },
                        "conditional_var_ratio_at_95": {
                            "CSCO": 8.852148606609475e-05,
                            "NFLX": 0.0008613682080784012,
                            "CVX": 0.0014152791840535961,
                            "PFE": 0.004839398608256321,
                            "MMM": 0.0019314256013221141
                        },
                        "entropic_var_ratio_at_95": {
                            "CSCO": 5.03469898928604e-05,
                            "NFLX": 0.000489907008946667,
                            "CVX": 0.0008049463462680617,
                            "PFE": 0.002752429535982739,
                            "MMM": 0.0010985069224433348
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "CSCO": 8.756020477313439e-06,
                            "NFLX": 8.520143530814538e-05,
                            "CVX": 0.00013999102441000674,
                            "PFE": 0.00047868461313602394,
                            "MMM": 0.00019104516730499496
                        },
                        "conditional_dar_ratio_at_95": {
                            "CSCO": 8.094587463525609e-06,
                            "NFLX": 7.876528748494994e-05,
                            "CVX": 0.00012941605083397796,
                            "PFE": 0.0004425246010459691,
                            "MMM": 0.00017661354495925616
                        },
                        "entropic_dar_ratio_at_95": {
                            "CSCO": 7.919304375471067e-06,
                            "NFLX": 7.705967581739099e-05,
                            "CVX": 0.00012661362944607897,
                            "PFE": 0.0004329420152797444,
                            "MMM": 0.00017278909217618199
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "CSCO": 9.325326235068146e-07,
                            "NFLX": 9.074112857583118e-06,
                            "CVX": 1.4909306984686822e-05,
                            "PFE": 5.098081020672122e-05,
                            "MMM": 2.0346669076074138e-05
                        },
                        "worst_realization_ratio": {
                            "CSCO": 2.970689650020838e-05,
                            "NFLX": 0.00028906627467651476,
                            "CVX": 0.0004749530775860183,
                            "PFE": 0.0016240521930617124,
                            "MMM": 0.0006481664846146886
                        },
                        "average_drawdown_ratio": {
                            "CSCO": 2.4430217470307836e-05,
                            "NFLX": 0.0002377209599673079,
                            "CVX": 0.0003905896724532308,
                            "PFE": 0.0013355803848224164,
                            "MMM": 0.0005330360973920889
                        },
                        "ulcer_index_ratio": {
                            "CSCO": 1.8154875859221192e-05,
                            "NFLX": 0.0001766580474605568,
                            "CVX": 0.00029025967631686906,
                            "PFE": 0.0009925124946567373,
                            "MMM": 0.0003961161700012969
                        },
                        "gini_mean_difference_ratio": {
                            "CSCO": 0.00019302020790551306,
                            "NFLX": 0.0018782046935176028,
                            "CVX": 0.003086001992176243,
                            "PFE": 0.010552259875143043,
                            "MMM": 0.004211454051312131
                        }
                    }
                },
                "allocation": {
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.5297069024670922,
                        "Shares": 18618,
                        "Purchase Value": 529729.6279447572,
                        "Current Value": 532102.4385794466,
                        "Net Value": 2372.8106346894056,
                        "Net Change": 0.004479286242484541,
                        "%Shares": 0.8291618419880645,
                        "%Purchase Value": 0.5297446211702407,
                        "%Current Value": 0.45533324172220124
                    },
                    "MMM": {
                        "Company Name": "3M Company",
                        "Sector": "Industrials",
                        "Industry": "Conglomerates",
                        "Market Cap": 74311114752,
                        "Volume (3 Months Average)": 4169252.3076923075,
                        "Current Price": 135.2700042725,
                        "Purchase Price": 89.3647994995,
                        "Price Diff": 45.905204772999994,
                        "Weight": 0.21140839088487615,
                        "Shares": 2366,
                        "Purchase Value": 211437.115615817,
                        "Current Value": 320048.83010873495,
                        "Net Value": 108611.71449291796,
                        "Net Change": 0.5136832962206426,
                        "%Shares": 0.10537098067159525,
                        "%Purchase Value": 0.2114431000353827,
                        "%Current Value": 0.2738737144521656
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.15491246193941888,
                        "Shares": 1070,
                        "Purchase Value": 154901.831054634,
                        "Current Value": 161291.805877724,
                        "Net Value": 6389.974823089986,
                        "Net Change": 0.04125177074786312,
                        "%Shares": 0.04765297942460141,
                        "%Purchase Value": 0.15490621532532284,
                        "%Current Value": 0.13802139495845728
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.09428293106635388,
                        "Shares": 201,
                        "Purchase Value": 94168.5,
                        "Current Value": 144659.702453607,
                        "Net Value": 50491.202453606995,
                        "Net Change": 0.5361793216798292,
                        "%Shares": 0.00895163445265877,
                        "%Purchase Value": 0.0941711653022211,
                        "%Current Value": 0.12378889192956655
                    },
                    "CSCO": {
                        "Company Name": "Cisco Systems, Inc.",
                        "Sector": "Technology",
                        "Industry": "Communication Equipment",
                        "Market Cap": 210511003648,
                        "Volume (3 Months Average)": 18805300.0,
                        "Current Price": 52.75,
                        "Purchase Price": 48.9177017212,
                        "Price Diff": 3.8322982788000033,
                        "Weight": 0.009689311830163534,
                        "Shares": 199,
                        "Purchase Value": 9734.6226425188,
                        "Current Value": 10497.25,
                        "Net Value": 762.6273574812003,
                        "Net Change": 0.07834174836425638,
                        "%Shares": 0.008862563463080075,
                        "%Purchase Value": 0.00973489816683267,
                        "%Current Value": 0.00898275693760935
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 28.302742272977973
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.07265192031871683,
                    "Expected Daily Return": 0.0002883012711060192,
                    "Expected Current Return": 0.055065542781249664,
                    "Net Value": 168628.32976178557,
                    "Net Change": 0.16863310254102548,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.024262947901168824,
                        "95.0% CVaR": 0.03155664286696439,
                        "99.0% CVaR": 0.05335872658843755,
                        "99.9% CVaR": 0.09299813810018669
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.04620867030453446,
                        "95.0% EVaR": 0.05548377227288516,
                        "99.0% EVaR": 0.074424064180971,
                        "99.9% EVaR": 0.09383878709272585
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.315545732996195,
                        "95.0% CDaR": 0.3450998502923125,
                        "99.0% CDaR": 0.36819136129850305,
                        "99.9% CDaR": 0.3814640494888121
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.3344160796165375,
                        "95.0% EDaR": 0.3527381685811961,
                        "99.0% EDaR": 0.3725513384383216,
                        "99.9% EDaR": 0.3832759180397929
                    },
                    "VaR": {
                        "90.0% VaR": 0.014846528232609749,
                        "95.0% VaR": 0.01931216166034006,
                        "99.0% VaR": 0.03610440477072316,
                        "99.9% VaR": 0.07799412755989481
                    },
                    "DaR": {
                        "90.0% DaR": 0.2636064652987002,
                        "95.0% DaR": 0.31903088041861377,
                        "99.0% DaR": 0.35915575095771834,
                        "99.9% DaR": 0.37643989172637515
                    },
                    "ERM": {
                        "90.0% ERM": 2.302395121580549,
                        "95.0% ERM": 2.9955423021404934,
                        "99.0% ERM": 4.604980214574594,
                        "99.9% ERM": 6.907565307568639
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "CSCO": 0.00023509126855944437,
                            "NFLX": 0.0022875818485777522,
                            "CVX": 0.0037586330000889197,
                            "PFE": 0.012852251000738077,
                            "MMM": 0.005129390783204629
                        },
                        "95.0% CVaR": {
                            "CSCO": 0.00030576215360519394,
                            "NFLX": 0.0029752527895029936,
                            "CVX": 0.004888517245922915,
                            "PFE": 0.01671577157561054,
                            "MMM": 0.006671339102322749
                        },
                        "99.0% CVaR": {
                            "CSCO": 0.0005170093417126797,
                            "NFLX": 0.005030817149842402,
                            "CVX": 0.008265931716745846,
                            "PFE": 0.02826448583196767,
                            "MMM": 0.011280482548168949
                        },
                        "99.9% CVaR": {
                            "CSCO": 0.0009010879613101782,
                            "NFLX": 0.008768137059687861,
                            "CVX": 0.01440657055498807,
                            "PFE": 0.049261755757523756,
                            "MMM": 0.01966058676667682
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "CSCO": 0.00044773021664918196,
                            "NFLX": 0.0043566888848850325,
                            "CVX": 0.00715829889279387,
                            "PFE": 0.024477051658492805,
                            "MMM": 0.009768900651713569
                        },
                        "95.0% EVaR": {
                            "CSCO": 0.0005375995720399474,
                            "NFLX": 0.005231172685985093,
                            "CVX": 0.008595127776053898,
                            "PFE": 0.029390137201117262,
                            "MMM": 0.011729735037688958
                        },
                        "99.0% EVaR": {
                            "CSCO": 0.000721117966824267,
                            "NFLX": 0.007016918925567712,
                            "CVX": 0.011529215030703574,
                            "PFE": 0.03942294057775234,
                            "MMM": 0.015733871680123104
                        },
                        "99.9% EVaR": {
                            "CSCO": 0.0009092332715533631,
                            "NFLX": 0.008847395910846056,
                            "CVX": 0.014536797560285187,
                            "PFE": 0.049707053332230675,
                            "MMM": 0.01983830701781056
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "CSCO": 0.0030574210092179943,
                            "NFLX": 0.029750576646273244,
                            "CVX": 0.048881966441497865,
                            "PFE": 0.1671467531150084,
                            "MMM": 0.06670901578419745
                        },
                        "95.0% CDaR": {
                            "CSCO": 0.0033437800680842164,
                            "NFLX": 0.03253702545507934,
                            "CVX": 0.05346026752058211,
                            "PFE": 0.18280177307145232,
                            "MMM": 0.0729570041771145
                        },
                        "99.0% CDaR": {
                            "CSCO": 0.0035675209192582895,
                            "NFLX": 0.034714160799439134,
                            "CVX": 0.05703743034693444,
                            "PFE": 0.19503350586199136,
                            "MMM": 0.07783874337087981
                        },
                        "99.9% CDaR": {
                            "CSCO": 0.003696124134191764,
                            "NFLX": 0.035965548747418884,
                            "CVX": 0.05909353515477532,
                            "PFE": 0.20206414042343168,
                            "MMM": 0.08064470102899442
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "CSCO": 0.0032402616822970903,
                            "NFLX": 0.0315297282391012,
                            "CVX": 0.05180521829940254,
                            "PFE": 0.17714250598986367,
                            "MMM": 0.070698365405873
                        },
                        "95.0% EDaR": {
                            "CSCO": 0.003417790115977364,
                            "NFLX": 0.03325718849307802,
                            "CVX": 0.05464353821393416,
                            "PFE": 0.18684784299964646,
                            "MMM": 0.07457180875856008
                        },
                        "99.0% EDaR": {
                            "CSCO": 0.0036097660974149285,
                            "NFLX": 0.035125232224308425,
                            "CVX": 0.05771284514088723,
                            "PFE": 0.19734301585173702,
                            "MMM": 0.07876047912397398
                        },
                        "99.9% EDaR": {
                            "CSCO": 0.0037136798936092965,
                            "NFLX": 0.036136377025421856,
                            "CVX": 0.05937421617322698,
                            "PFE": 0.20302389970298845,
                            "MMM": 0.08102774524454628
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "CSCO": 0.00014385264190175726,
                            "NFLX": 0.0013997742004663461,
                            "CVX": 0.0022999122439343257,
                            "PFE": 0.007864308496736819,
                            "MMM": 0.0031386806495705
                        },
                        "95.0% VaR": {
                            "CSCO": 0.0001871215567806457,
                            "NFLX": 0.0018208072098636007,
                            "CVX": 0.00299169451359657,
                            "PFE": 0.010229785351579816,
                            "MMM": 0.004082753028519429
                        },
                        "99.0% VaR": {
                            "CSCO": 0.0003498268368999002,
                            "NFLX": 0.0034040291123582553,
                            "CVX": 0.005593022240025114,
                            "PFE": 0.019124752451173743,
                            "MMM": 0.0076327741302661435
                        },
                        "99.9% VaR": {
                            "CSCO": 0.00075570942421879,
                            "NFLX": 0.007353514965635245,
                            "CVX": 0.012082262339014596,
                            "PFE": 0.0413140277952401,
                            "MMM": 0.01648861303578607
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "CSCO": 0.00255416524735468,
                            "NFLX": 0.024853590241439634,
                            "CVX": 0.04083592659656823,
                            "PFE": 0.1396341644567039,
                            "MMM": 0.05572861875663372
                        },
                        "95.0% DaR": {
                            "CSCO": 0.0030911896894290926,
                            "NFLX": 0.03007916656105267,
                            "CVX": 0.04942185920990492,
                            "PFE": 0.16899285976412437,
                            "MMM": 0.06744580519410272
                        },
                        "99.0% DaR": {
                            "CSCO": 0.0034799720729319296,
                            "NFLX": 0.03386225697099276,
                            "CVX": 0.05563770170138176,
                            "PFE": 0.19024728068780156,
                            "MMM": 0.0759285395246103
                        },
                        "99.9% DaR": {
                            "CSCO": 0.003647443502859362,
                            "NFLX": 0.03549185642657818,
                            "CVX": 0.05831523050521381,
                            "PFE": 0.19940280937276264,
                            "MMM": 0.07958255191896114
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "CSCO": 0.022308624329666574,
                            "NFLX": 0.2170765609288518,
                            "CVX": 0.35666969728766995,
                            "PFE": 1.2195945903177983,
                            "MMM": 0.4867456487165622
                        },
                        "95.0% ERM": {
                            "CSCO": 0.02902474351848079,
                            "NFLX": 0.2824285088908466,
                            "CVX": 0.4640468337091555,
                            "PFE": 1.5867594369513425,
                            "MMM": 0.633282779070668
                        },
                        "99.0% ERM": {
                            "CSCO": 0.044619089351600666,
                            "NFLX": 0.4341710329194193,
                            "CVX": 0.7133688235147561,
                            "PFE": 2.4392898098047793,
                            "MMM": 0.9735314589840385
                        },
                        "99.9% ERM": {
                            "CSCO": 0.06692955437353476,
                            "NFLX": 0.6512655049099868,
                            "CVX": 1.0700679497418422,
                            "PFE": 3.65898502929176,
                            "MMM": 1.4603172692515147
                        }
                    }
                }
            }
        },
        {
            "name": "CVaR 99.9%",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.030716877538656227,
                    "annual_standard_deviation": 0.2465737820656314,
                    "annual_sharpe_ratio": 0.1245747916965487,
                    "annual_sortino_ratio": 0.18022793089717168,
                    "cvar_900": -0.02670940284544024,
                    "cvar_950": -0.0343833018580712,
                    "cvar_990": -0.05799332237592604,
                    "cvar_999": -0.0767596182069276,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.22195155762380303
                        }
                    ]
                },
                "weights": [
                    5.909024202288758e-10,
                    1.047063442637516e-09,
                    5.7315618498764e-09,
                    6.946305782363809e-10,
                    4.787217110128161e-10,
                    0.7864098616604909,
                    0.21359012933106084,
                    4.6556812549810547e-10
                ],
                "position": [
                    0.2465737820656314,
                    0.030716877538656227
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.00012189237118514376,
                        "annual_mean_return": 0.030716877538656227,
                        "daily_variance": 0.00024126440477043452,
                        "annual_variance": 0.0607986300021495,
                        "daily_standard_deviation": 0.015532688266054737,
                        "annual_standard_deviation": 0.2465737820656314,
                        "daily_semi_variance": 0.00011526816994631982,
                        "annual_semi_variance": 0.029047578826472593,
                        "daily_semi_deviation": 0.010736301502208282,
                        "annual_semi_deviation": 0.1704335026527138,
                        "mean_absolute_deviation": 0.011055260237278043
                    },
                    "stats_moments": {
                        "skew": 0.19295696019958983,
                        "kurtosis": 7.258949289026928,
                        "first_lower_partial_moment": 0.005527630118639022,
                        "fourth_central_moment": 4.2253264412367975e-07,
                        "fourth_lower_partial_moment": 1.8602999300322088e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.022131325135501017,
                        "conditional_var_at_95": 0.0343833018580712,
                        "entropic_var_at_95": 0.05125215726046722,
                        "drawdown_at_risk_at_95": 0.5225518981153675,
                        "conditional_dar_at_95": 0.563064414953166,
                        "entropic_dar_at_95": 0.5741426362881055,
                        "entropic_risk_measure_at_95": 2.9957307903471104,
                        "worst_realization": 0.07706228029471132,
                        "average_drawdown": 0.1717204016447866,
                        "max_drawdown": 0.6321580500502282,
                        "ulcer_index": 0.2351072752594178,
                        "gini_mean_difference": 0.016294652560341273
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.007847474248970048,
                        "annual_sharpe_ratio": 0.1245747916965487,
                        "daily_sortino_ratio": 0.011353292487182153,
                        "annual_sortino_ratio": 0.18022793089717168,
                        "mean_absolute_deviation_ratio": 0.011025735131419695,
                        "calmar_ratio": 0.0001928194557918843,
                        "value_at_risk_ratio_at_95": 0.005507685167464976,
                        "conditional_var_ratio_at_95": 0.0035451037159926076,
                        "entropic_var_ratio_at_95": 0.002378287621449333,
                        "drawdown_at_risk_ratio_at_95": 0.00023326366553209362,
                        "conditional_dar_ratio_at_95": 0.0002164803314648865,
                        "entropic_dar_ratio_at_95": 0.00021230329099610365,
                        "entropic_risk_measure_ratio_at_95": 4.068869324904201e-05,
                        "worst_realization_ratio": 0.001581738442192309,
                        "average_drawdown_ratio": 0.0007098304570547478,
                        "ulcer_index_ratio": 0.0005184542717814559,
                        "gini_mean_difference_ratio": 0.007480513667521295
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "PFE": 9.585736362470421e-05,
                            "MMM": 2.603500756043955e-05
                        },
                        "annual_mean_return": {
                            "PFE": 0.024156055633425464,
                            "MMM": 0.006560821905230767
                        },
                        "daily_variance": {
                            "PFE": 0.0001897327088883154,
                            "MMM": 5.1531695882119145e-05
                        },
                        "annual_variance": {
                            "PFE": 0.047812642639855484,
                            "MMM": 0.012985987362294024
                        },
                        "daily_standard_deviation": {
                            "PFE": 0.012215059340562367,
                            "MMM": 0.003317628925492371
                        },
                        "annual_standard_deviation": {
                            "PFE": 0.19390805559014793,
                            "MMM": 0.0526657264754835
                        },
                        "daily_semi_variance": {
                            "PFE": 9.064802639794139e-05,
                            "MMM": 2.462014354837844e-05
                        },
                        "annual_semi_variance": {
                            "PFE": 0.02284330265228123,
                            "MMM": 0.006204276174191367
                        },
                        "daily_semi_deviation": {
                            "PFE": 0.008443133455156467,
                            "MMM": 0.0022931680470518155
                        },
                        "annual_semi_deviation": {
                            "PFE": 0.13403058845084118,
                            "MMM": 0.03640291420187261
                        },
                        "mean_absolute_deviation": {
                            "PFE": 0.008693965752137694,
                            "MMM": 0.002361294485140351
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "PFE": 0.15174325774395958,
                            "MMM": 0.04121370245563026
                        },
                        "kurtosis": {
                            "PFE": 5.708509357608997,
                            "MMM": 1.5504399314179318
                        },
                        "first_lower_partial_moment": {
                            "PFE": 0.004346982876068847,
                            "MMM": 0.0011806472425701755
                        },
                        "fourth_central_moment": {
                            "PFE": 3.322838412057062e-07,
                            "MMM": 9.024880291797354e-08
                        },
                        "fourth_lower_partial_moment": {
                            "PFE": 1.4629582238026336e-07,
                            "MMM": 3.973417062295751e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "PFE": 0.017404292494958368,
                            "MMM": 0.004727032640542649
                        },
                        "conditional_var_at_95": {
                            "PFE": 0.02703936790121942,
                            "MMM": 0.007343933956851782
                        },
                        "entropic_var_at_95": {
                            "PFE": 0.04030520226409308,
                            "MMM": 0.010946954996374141
                        },
                        "drawdown_at_risk_at_95": {
                            "PFE": 0.41093996960926454,
                            "MMM": 0.11161192850610296
                        },
                        "conditional_dar_at_95": {
                            "PFE": 0.4427994126582001,
                            "MMM": 0.12026500229496588
                        },
                        "entropic_dar_at_95": {
                            "PFE": 0.451511435244136,
                            "MMM": 0.12263120104396952
                        },
                        "entropic_risk_measure_at_95": {
                            "PFE": 2.3558722576316975,
                            "MMM": 0.6398585327154129
                        },
                        "worst_realization": {
                            "PFE": 0.060602537731740735,
                            "MMM": 0.016459742562970593
                        },
                        "average_drawdown": {
                            "PFE": 0.13504261851828503,
                            "MMM": 0.0366777831265016
                        },
                        "max_drawdown": {
                            "PFE": 0.4971353291659835,
                            "MMM": 0.1350227208842447
                        },
                        "ulcer_index": {
                            "PFE": 0.18489068147771184,
                            "MMM": 0.05021659378170596
                        },
                        "gini_mean_difference": {
                            "PFE": 0.012814275581220483,
                            "MMM": 0.0034803769791207904
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "PFE": 0.006171331194110918,
                            "MMM": 0.0016761430548591302
                        },
                        "annual_sharpe_ratio": {
                            "PFE": 0.0979668455869966,
                            "MMM": 0.026607946109552107
                        },
                        "daily_sortino_ratio": {
                            "PFE": 0.008928341254666508,
                            "MMM": 0.0024249512325156455
                        },
                        "annual_sortino_ratio": {
                            "PFE": 0.1417330234809959,
                            "MMM": 0.03849490741617578
                        },
                        "mean_absolute_deviation_ratio": {
                            "PFE": 0.008670746917514951,
                            "MMM": 0.0023549882139047434
                        },
                        "calmar_ratio": {
                            "PFE": 0.00015163512292074404,
                            "MMM": 4.118433287114027e-05
                        },
                        "value_at_risk_ratio_at_95": {
                            "PFE": 0.004331297969633943,
                            "MMM": 0.0011763871978310331
                        },
                        "conditional_var_ratio_at_95": {
                            "PFE": 0.002787904547980533,
                            "MMM": 0.000757199168012075
                        },
                        "entropic_var_ratio_at_95": {
                            "PFE": 0.0018703088562214087,
                            "MMM": 0.0005079787652279246
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "PFE": 0.00018344084859403016,
                            "MMM": 4.982281693806347e-05
                        },
                        "conditional_dar_ratio_at_95": {
                            "PFE": 0.0001702422690531373,
                            "MMM": 4.6238062411749224e-05
                        },
                        "entropic_dar_ratio_at_95": {
                            "PFE": 0.00016695740320633995,
                            "MMM": 4.5345887789763715e-05
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "PFE": 3.199798991737751e-05,
                            "MMM": 8.690703331664496e-06
                        },
                        "worst_realization_ratio": {
                            "PFE": 0.0012438947207130955,
                            "MMM": 0.0003378437214792137
                        },
                        "average_drawdown_ratio": {
                            "PFE": 0.0005582176765635023,
                            "MMM": 0.00015161278049124552
                        },
                        "ulcer_index_ratio": {
                            "PFE": 0.0004077175558218478,
                            "MMM": 0.0001107367159596081
                        },
                        "gini_mean_difference_ratio": {
                            "PFE": 0.00588274977141928,
                            "MMM": 0.0015977638961020152
                        }
                    }
                },
                "allocation": {
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.7864098616604909,
                        "Shares": 27639,
                        "Purchase Value": 786400.1067120606,
                        "Current Value": 789922.6178911444,
                        "Net Value": 3522.5111790837254,
                        "Net Change": 0.004479286242484563,
                        "%Shares": 0.9204102700722635,
                        "%Purchase Value": 0.7864142798509424,
                        "%Current Value": 0.7095848871547003
                    },
                    "MMM": {
                        "Company Name": "3M Company",
                        "Sector": "Industrials",
                        "Industry": "Conglomerates",
                        "Market Cap": 74311114752,
                        "Volume (3 Months Average)": 4169252.3076923075,
                        "Current Price": 135.2700042725,
                        "Purchase Price": 89.3647994995,
                        "Price Diff": 45.905204772999994,
                        "Weight": 0.21359012933106084,
                        "Shares": 2390,
                        "Purchase Value": 213581.87080380498,
                        "Current Value": 323295.31021127495,
                        "Net Value": 109713.43940746997,
                        "Net Change": 0.5136832962206426,
                        "%Shares": 0.07958972992773652,
                        "%Purchase Value": 0.21358572014905772,
                        "%Current Value": 0.2904151128452998
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 18.022484134417027
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.030716877538656227,
                    "Expected Daily Return": 0.00012189237118514376,
                    "Expected Current Return": 0.023281442896362456,
                    "Net Value": 113235.95058655366,
                    "Net Change": 0.11323799141645738,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.02670940284544024,
                        "95.0% CVaR": 0.0343833018580712,
                        "99.0% CVaR": 0.05799332237592604,
                        "99.9% CVaR": 0.0767596182069276
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.04342451366613208,
                        "95.0% EVaR": 0.05125215726046722,
                        "99.0% EVaR": 0.06643153040303043,
                        "99.9% EVaR": 0.07701200592270642
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.5104795538760509,
                        "95.0% CDaR": 0.563064414953166,
                        "99.0% CDaR": 0.5955783882045371,
                        "99.9% CDaR": 0.6315260584000082
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.5419291759060931,
                        "95.0% EDaR": 0.5741426362881055,
                        "99.0% EDaR": 0.61132614707158,
                        "99.9% EDaR": 0.6335387654209769
                    },
                    "VaR": {
                        "90.0% VaR": 0.016694392593125565,
                        "95.0% VaR": 0.022131325135501017,
                        "99.0% VaR": 0.041625887900960425,
                        "99.9% VaR": 0.07237321113759836
                    },
                    "DaR": {
                        "90.0% DaR": 0.4201081027772584,
                        "95.0% DaR": 0.5225518981153675,
                        "99.0% DaR": 0.5730725344525133,
                        "99.9% DaR": 0.6223667591214561
                    },
                    "ERM": {
                        "90.0% ERM": 2.3025836097871664,
                        "95.0% ERM": 2.9957307903471104,
                        "99.0% ERM": 4.605168702781211,
                        "99.9% ERM": 6.907753795775257
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "PFE": 0.021004537985935275,
                            "MMM": 0.005704864859504965
                        },
                        "95.0% CVaR": {
                            "PFE": 0.02703936790121942,
                            "MMM": 0.007343933956851782
                        },
                        "99.0% CVaR": {
                            "PFE": 0.045606521037728234,
                            "MMM": 0.012386801338197808
                        },
                        "99.9% CVaR": {
                            "PFE": 0.060364521279012706,
                            "MMM": 0.016395096927914903
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "PFE": 0.03414946609249073,
                            "MMM": 0.009275047573641356
                        },
                        "95.0% EVaR": {
                            "PFE": 0.04030520226409308,
                            "MMM": 0.010946954996374141
                        },
                        "99.0% EVaR": {
                            "PFE": 0.052242411104764915,
                            "MMM": 0.014189119298265518
                        },
                        "99.9% EVaR": {
                            "PFE": 0.06056300146945113,
                            "MMM": 0.016449004453255294
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "PFE": 0.4014461589605813,
                            "MMM": 0.10903339491546966
                        },
                        "95.0% CDaR": {
                            "PFE": 0.4427994126582001,
                            "MMM": 0.12026500229496588
                        },
                        "99.0% CDaR": {
                            "PFE": 0.4683687220951836,
                            "MMM": 0.12720966610935355
                        },
                        "99.9% CDaR": {
                            "PFE": 0.49663832469528624,
                            "MMM": 0.134887733704722
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "PFE": 0.4261784520933011,
                            "MMM": 0.11575072381279207
                        },
                        "95.0% EDaR": {
                            "PFE": 0.451511435244136,
                            "MMM": 0.12263120104396952
                        },
                        "99.0% EDaR": {
                            "PFE": 0.4807529150788399,
                            "MMM": 0.1305732319927401
                        },
                        "99.9% EDaR": {
                            "PFE": 0.498221137359468,
                            "MMM": 0.13531762806150893
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "PFE": 0.01312863508793443,
                            "MMM": 0.003565757505191136
                        },
                        "95.0% VaR": {
                            "PFE": 0.017404292494958368,
                            "MMM": 0.004727032640542649
                        },
                        "99.0% VaR": {
                            "PFE": 0.03273500904058103,
                            "MMM": 0.008890878860379401
                        },
                        "99.9% VaR": {
                            "PFE": 0.05691500747136013,
                            "MMM": 0.015458203666238235
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "PFE": 0.33037715796370065,
                            "MMM": 0.08973094481355781
                        },
                        "95.0% DaR": {
                            "PFE": 0.41093996960926454,
                            "MMM": 0.11161192850610296
                        },
                        "99.0% DaR": {
                            "PFE": 0.45066989660006435,
                            "MMM": 0.12240263785244897
                        },
                        "99.9% DaR": {
                            "PFE": 0.4894353613518455,
                            "MMM": 0.13293139776961063
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "PFE": 1.8107744743467076,
                            "MMM": 0.491809135440459
                        },
                        "95.0% ERM": {
                            "PFE": 2.3558722576316975,
                            "MMM": 0.6398585327154129
                        },
                        "99.0% ERM": {
                            "PFE": 3.6215501151019414,
                            "MMM": 0.9836185876792698
                        },
                        "99.9% ERM": {
                            "PFE": 5.4323257558571765,
                            "MMM": 1.4754280399180808
                        }
                    }
                }
            }
        },
        {
            "name": "HRP",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.15516226590190704,
                    "annual_standard_deviation": 0.2249374557536555,
                    "annual_sharpe_ratio": 0.6898018179410543,
                    "annual_sortino_ratio": 0.9612224894725091,
                    "cvar_900": -0.024525782340269645,
                    "cvar_950": -0.03281746310915763,
                    "cvar_990": -0.05809105702443222,
                    "cvar_999": -0.10808525806218999,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.08376987752103285
                        }
                    ]
                },
                "weights": [
                    0.11916292341931652,
                    0.18028390735584074,
                    0.05740281000894311,
                    0.04367748007072976,
                    0.10492202340710839,
                    0.19291882414448006,
                    0.1845121386309221,
                    0.1171198929626593
                ],
                "position": [
                    0.2249374557536555,
                    0.15516226590190704
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.00061572327738852,
                        "annual_mean_return": 0.15516226590190704,
                        "daily_variance": 0.00020078118651161797,
                        "annual_variance": 0.05059685900092773,
                        "daily_standard_deviation": 0.014169727820661128,
                        "annual_standard_deviation": 0.2249374557536555,
                        "daily_semi_variance": 0.00010340078572423813,
                        "annual_semi_variance": 0.02605699800250801,
                        "daily_semi_deviation": 0.010168617689943807,
                        "annual_semi_deviation": 0.1614218015093005,
                        "mean_absolute_deviation": 0.009467200745916355
                    },
                    "stats_moments": {
                        "skew": -0.09693626957116058,
                        "kurtosis": 14.615851031074797,
                        "first_lower_partial_moment": 0.004733600372958178,
                        "fourth_central_moment": 5.892100428731809e-07,
                        "fourth_lower_partial_moment": 3.018222804838193e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.019457060662399276,
                        "conditional_var_at_95": 0.03281746310915763,
                        "entropic_var_at_95": 0.06301028662948027,
                        "drawdown_at_risk_at_95": 0.23533240828855484,
                        "conditional_dar_at_95": 0.2667825500085255,
                        "entropic_dar_at_95": 0.28326279842154767,
                        "entropic_risk_measure_at_95": 2.9952169124547035,
                        "worst_realization": 0.1091774293871318,
                        "average_drawdown": 0.08654153091606849,
                        "max_drawdown": 0.32243109953483834,
                        "ulcer_index": 0.11847800669066914,
                        "gini_mean_difference": 0.014113949844827662
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.043453430099816254,
                        "annual_sharpe_ratio": 0.6898018179410543,
                        "daily_sortino_ratio": 0.0605513252796824,
                        "annual_sortino_ratio": 0.9612224894725091,
                        "mean_absolute_deviation_ratio": 0.06503752206311988,
                        "calmar_ratio": 0.0019096274468461804,
                        "value_at_risk_ratio_at_95": 0.03164523604422963,
                        "conditional_var_ratio_at_95": 0.01876206199548386,
                        "entropic_var_ratio_at_95": 0.009771789819163353,
                        "drawdown_at_risk_ratio_at_95": 0.0026163981487562294,
                        "conditional_dar_ratio_at_95": 0.0023079593375535373,
                        "entropic_dar_ratio_at_95": 0.0021736821101096706,
                        "entropic_risk_measure_ratio_at_95": 0.00020556884372154185,
                        "worst_realization_ratio": 0.005639657215276881,
                        "average_drawdown_ratio": 0.007114772189385852,
                        "ulcer_index_ratio": 0.005196941563982372,
                        "gini_mean_difference_ratio": 0.04362515696583434
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 7.337138575093879e-05,
                            "CSCO": 0.00011100499829754657,
                            "NFLX": 3.534424631001699e-05,
                            "AMD": 2.6893241177221496e-05,
                            "CVX": 6.460293212245979e-05,
                            "PFE": 0.0001187846106721788,
                            "MMM": 0.00011360841871579632,
                            "MSFT": 7.211344434236125e-05
                        },
                        "annual_mean_return": {
                            "AAPL": 0.018489589209236577,
                            "CSCO": 0.027973259570981734,
                            "NFLX": 0.008906750070124281,
                            "AMD": 0.006777096776659817,
                            "CVX": 0.016279938894859868,
                            "PFE": 0.02993372188938906,
                            "MMM": 0.02862932151638067,
                            "MSFT": 0.018172587974275033
                        },
                        "daily_variance": {
                            "AAPL": 2.392567315232344e-05,
                            "CSCO": 3.6197616827856315e-05,
                            "NFLX": 1.1525404302696577e-05,
                            "AMD": 8.76961627243867e-06,
                            "CVX": 2.1066368350878978e-05,
                            "PFE": 3.873447041215488e-05,
                            "MMM": 3.7046566120112686e-05,
                            "MSFT": 2.351547107315643e-05
                        },
                        "annual_variance": {
                            "AAPL": 0.006029269634385507,
                            "CSCO": 0.009121799440619792,
                            "NFLX": 0.0029044018842795376,
                            "AMD": 0.0022099433006545445,
                            "CVX": 0.005308724824421502,
                            "PFE": 0.00976108654386303,
                            "MMM": 0.009335734662268396,
                            "MSFT": 0.005925898710435421
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.0016885061911660006,
                            "CSCO": 0.00255457389767755,
                            "NFLX": 0.0008133821939678462,
                            "AMD": 0.0006188980044945914,
                            "CVX": 0.0014867165140717618,
                            "PFE": 0.0027336072296092707,
                            "MMM": 0.00261448678400826,
                            "MSFT": 0.001659557005665847
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.026804204814108747,
                            "CSCO": 0.040552603433950556,
                            "NFLX": 0.012912042036522135,
                            "AMD": 0.009824701240840946,
                            "CVX": 0.02360089299772045,
                            "PFE": 0.04339466947004623,
                            "MMM": 0.04150369101930539,
                            "MSFT": 0.026344650741161046
                        },
                        "daily_semi_variance": {
                            "AAPL": 1.2321539910754545e-05,
                            "CSCO": 1.8641497674029686e-05,
                            "NFLX": 5.9354956577038784e-06,
                            "AMD": 4.516285757768209e-06,
                            "CVX": 1.0849019660071913e-05,
                            "PFE": 1.994795799753536e-05,
                            "MMM": 1.90787001100969e-05,
                            "MSFT": 1.211028895627764e-05
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.003105028057510145,
                            "CSCO": 0.004697657413855481,
                            "NFLX": 0.0014957449057413773,
                            "AMD": 0.0011381040109575888,
                            "CVX": 0.002733952954338122,
                            "PFE": 0.005026885415378911,
                            "MMM": 0.004807832427744419,
                            "MSFT": 0.0030517928169819654
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.001211722211067081,
                            "CSCO": 0.0018332381295507925,
                            "NFLX": 0.0005837072293094223,
                            "AMD": 0.0004441395964993907,
                            "CVX": 0.0010669119432822206,
                            "PFE": 0.001961717767918718,
                            "MMM": 0.0018762333968917585,
                            "MSFT": 0.0011909474154244224
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.019235493771460888,
                            "CSCO": 0.029101753108515642,
                            "NFLX": 0.009266065003339702,
                            "AMD": 0.007050497518403767,
                            "CVX": 0.01693670203637643,
                            "PFE": 0.031141304138457906,
                            "MMM": 0.029784281818137245,
                            "MSFT": 0.018905704114608908
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.0011281393174809268,
                            "CSCO": 0.0017067839421959306,
                            "NFLX": 0.000543443925734361,
                            "AMD": 0.00041350347190535953,
                            "CVX": 0.0009933178582628298,
                            "PFE": 0.0018264012358419277,
                            "MMM": 0.0017468134564772877,
                            "MSFT": 0.0011087975380177318
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.01155120926746243,
                            "CSCO": -0.017476049442787918,
                            "NFLX": -0.005564414265169024,
                            "AMD": -0.004233931982325254,
                            "CVX": -0.01017074954494308,
                            "PFE": -0.018700831142620642,
                            "MMM": -0.017885918409478417,
                            "MSFT": -0.011353165516373815
                        },
                        "kurtosis": {
                            "AAPL": 1.7416675371241044,
                            "CSCO": 2.635002733213058,
                            "NFLX": 0.8389909198558018,
                            "AMD": 0.6383835421265245,
                            "CVX": 1.533524663997239,
                            "PFE": 2.8196727947858364,
                            "MMM": 2.696801931654579,
                            "MSFT": 1.711806908317654
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.0005640696587404635,
                            "CSCO": 0.0008533919710979654,
                            "NFLX": 0.00027172196286718057,
                            "AMD": 0.0002067517359526798,
                            "CVX": 0.000496658929131415,
                            "PFE": 0.000913200617920964,
                            "MMM": 0.000873406728238644,
                            "MSFT": 0.000554398769008866
                        },
                        "fourth_central_moment": {
                            "AAPL": 7.021199121678906e-08,
                            "CSCO": 1.062250887824795e-07,
                            "NFLX": 3.382231214641042e-08,
                            "AMD": 2.5735209905067184e-08,
                            "CVX": 6.182110991004322e-08,
                            "PFE": 1.1366970864521273e-07,
                            "MMM": 1.087164051133479e-07,
                            "MSFT": 6.900821715383084e-08
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 3.596602529553683e-08,
                            "CSCO": 5.4413700052673456e-08,
                            "NFLX": 1.7325447023078615e-08,
                            "AMD": 1.3182836640734225e-08,
                            "CVX": 3.166780437771012e-08,
                            "PFE": 5.822719945154387e-08,
                            "MMM": 5.568987445853152e-08,
                            "MSFT": 3.5349393184010646e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.002318560229678481,
                            "CSCO": 0.0035077949218769644,
                            "NFLX": 0.0011168899565361864,
                            "AMD": 0.0008498353793169244,
                            "CVX": 0.0020414741742537847,
                            "PFE": 0.0037536332642978867,
                            "MMM": 0.0035900638742908763,
                            "MSFT": 0.002278808862148172
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.0039106248432927955,
                            "CSCO": 0.005916460478825096,
                            "NFLX": 0.001883814599830475,
                            "AMD": 0.0014333840909221416,
                            "CVX": 0.003443274632500953,
                            "PFE": 0.006331106394423543,
                            "MMM": 0.0060552203027120655,
                            "MSFT": 0.0038435777666505624
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.007508489960257941,
                            "CSCO": 0.011359740677174192,
                            "NFLX": 0.0036169675120011043,
                            "AMD": 0.0027521305385100944,
                            "CVX": 0.006611166768626938,
                            "PFE": 0.012155870405565988,
                            "MMM": 0.011626162741752802,
                            "MSFT": 0.0073797580255912125
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.028042897746972387,
                            "CSCO": 0.04242664609372071,
                            "NFLX": 0.013508741521934943,
                            "AMD": 0.010278726573020192,
                            "CVX": 0.02469155245090294,
                            "PFE": 0.045400051490116694,
                            "MMM": 0.0434216859424866,
                            "MSFT": 0.02756210646940038
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.031790588576275904,
                            "CSCO": 0.04809660052989197,
                            "NFLX": 0.015314068031840754,
                            "AMD": 0.01165238951121584,
                            "CVX": 0.02799136495660258,
                            "PFE": 0.05146737584991069,
                            "MMM": 0.04922461885148397,
                            "MSFT": 0.03124554370130381
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.03375442315584817,
                            "CSCO": 0.05106772410798649,
                            "NFLX": 0.01626008060039365,
                            "AMD": 0.01237220523283629,
                            "CVX": 0.02972050596634865,
                            "PFE": 0.05464672599535986,
                            "MMM": 0.05226542473133955,
                            "MSFT": 0.033175708631435
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 0.3569188035630815,
                            "CSCO": 0.5399894083556311,
                            "NFLX": 0.17193386736121052,
                            "AMD": 0.13082352700125302,
                            "CVX": 0.3142642189979393,
                            "PFE": 0.5778337248084214,
                            "MMM": 0.5526538781805247,
                            "MSFT": 0.35079948418664175
                        },
                        "worst_realization": {
                            "AAPL": 0.013009901657176623,
                            "CSCO": 0.019682933564978515,
                            "NFLX": 0.006267091236374329,
                            "AMD": 0.004768594996229955,
                            "CVX": 0.011455116801684567,
                            "PFE": 0.02106238130048247,
                            "MMM": 0.020144560986446174,
                            "MSFT": 0.012786848843759172
                        },
                        "average_drawdown": {
                            "AAPL": 0.010312541821141882,
                            "CSCO": 0.015602045342105119,
                            "NFLX": 0.004967727057058156,
                            "AMD": 0.003779915991877025,
                            "CVX": 0.009080112532462733,
                            "PFE": 0.0166954903839911,
                            "MMM": 0.015967962949717862,
                            "MSFT": 0.010135734837714612
                        },
                        "max_drawdown": {
                            "AAPL": 0.03842183242187596,
                            "CSCO": 0.05812913847718066,
                            "NFLX": 0.01850845114757295,
                            "AMD": 0.014082977924116386,
                            "CVX": 0.033830123372574,
                            "PFE": 0.062203028589872825,
                            "MMM": 0.05949245173629274,
                            "MSFT": 0.037763095865352814
                        },
                        "ulcer_index": {
                            "AAPL": 0.014118185638153476,
                            "CSCO": 0.021359677981925274,
                            "NFLX": 0.006800970508302771,
                            "AMD": 0.005174820776051489,
                            "CVX": 0.012430952191225933,
                            "PFE": 0.02285663773774573,
                            "MMM": 0.021860630395224064,
                            "MSFT": 0.013876131462040402
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.0016818595245032728,
                            "CSCO": 0.002544518026249893,
                            "NFLX": 0.0008101803814183943,
                            "AMD": 0.0006164617630667396,
                            "CVX": 0.0014808641759857617,
                            "PFE": 0.002722846608098319,
                            "MMM": 0.002604195070398723,
                            "MSFT": 0.0016530242951065576
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.0051780377632910275,
                            "CSCO": 0.007833954166408775,
                            "NFLX": 0.0024943489922566423,
                            "AMD": 0.0018979363271895732,
                            "CVX": 0.004559221810052069,
                            "PFE": 0.008382984639900908,
                            "MMM": 0.00801768531856638,
                            "MSFT": 0.0050892610821508776
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.08219880120581517,
                            "CSCO": 0.12436016703957556,
                            "NFLX": 0.0395965626990939,
                            "AMD": 0.03012880515587356,
                            "CVX": 0.07237540248827723,
                            "PFE": 0.13307575560991292,
                            "MMM": 0.1272768086598019,
                            "MSFT": 0.08078951508270409
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.007215472937240918,
                            "CSCO": 0.010916429516995639,
                            "NFLX": 0.0034758162208193225,
                            "AMD": 0.002644729303159603,
                            "CVX": 0.0063531675683262704,
                            "PFE": 0.011681490473346259,
                            "MMM": 0.011172454524290817,
                            "MSFT": 0.007091764735503569
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 0.11454208190193738,
                            "CSCO": 0.17329294624041244,
                            "NFLX": 0.05517687193951376,
                            "AMD": 0.04198377612747276,
                            "CVX": 0.1008534085398736,
                            "PFE": 0.1854379124102663,
                            "MMM": 0.17735721723271167,
                            "MSFT": 0.11257827508032117
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.007750061260989663,
                            "CSCO": 0.011725218602280953,
                            "NFLX": 0.0037333365224417165,
                            "AMD": 0.002840675073761566,
                            "CVX": 0.006823868412246993,
                            "PFE": 0.012546962281687767,
                            "MMM": 0.012000212287122032,
                            "MSFT": 0.007617187622589194
                        },
                        "calmar_ratio": {
                            "AAPL": 0.00022755678920795633,
                            "CSCO": 0.0003442750977113875,
                            "NFLX": 0.0001096179815191744,
                            "AMD": 8.34077147521426e-05,
                            "CVX": 0.00020036197567685157,
                            "PFE": 0.0003684030815995907,
                            "MMM": 0.0003523494442058963,
                            "MSFT": 0.00022365536217318103
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.0037709388393247297,
                            "CSCO": 0.005705126803251606,
                            "NFLX": 0.0018165254723350717,
                            "AMD": 0.0013821841666553786,
                            "CVX": 0.003320282196956131,
                            "PFE": 0.006104961727427297,
                            "MMM": 0.00583893018000115,
                            "MSFT": 0.003706286658278262
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.0022357421567563117,
                            "CSCO": 0.0033824978465983526,
                            "NFLX": 0.001076995080102772,
                            "AMD": 0.0008194795888935425,
                            "CVX": 0.001968553507855776,
                            "PFE": 0.003619554938694583,
                            "MMM": 0.003461828183912673,
                            "MSFT": 0.0021974106926698476
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.0011644350418906194,
                            "CSCO": 0.0017616964504587936,
                            "NFLX": 0.0005609281944367585,
                            "AMD": 0.0004268071550818673,
                            "CVX": 0.0010252759601356008,
                            "PFE": 0.0018851622016999954,
                            "MMM": 0.001803013837785702,
                            "MSFT": 0.0011444709776740158
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 0.00031177765223468006,
                            "CSCO": 0.00047169448145636126,
                            "NFLX": 0.0001501886058408043,
                            "AMD": 0.00011427767799939445,
                            "CVX": 0.0002745177878061162,
                            "PFE": 0.0005047524543518462,
                            "MMM": 0.0004827572179369974,
                            "MSFT": 0.00030643227113002954
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 0.00027502318179578865,
                            "CSCO": 0.00041608792739254946,
                            "NFLX": 0.0001324833513619519,
                            "AMD": 0.00010080584797004929,
                            "CVX": 0.00024215576363744663,
                            "PFE": 0.00044524880157410156,
                            "MMM": 0.0004258465132452094,
                            "MSFT": 0.00027030795057644033
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 0.00025902231482493704,
                            "CSCO": 0.0003918799041600603,
                            "NFLX": 0.00012477546118646397,
                            "AMD": 9.494095704441695e-05,
                            "CVX": 0.00022806712523653963,
                            "PFE": 0.00041934419674624987,
                            "MMM": 0.00040107073484011086,
                            "MSFT": 0.000254581416070892
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 2.4496184381787535e-05,
                            "CSCO": 3.706075437674175e-05,
                            "NFLX": 1.1800229279905783e-05,
                            "AMD": 8.978729074810604e-06,
                            "CVX": 2.156869903272382e-05,
                            "PFE": 3.965809961150023e-05,
                            "MMM": 3.7929946990947494e-05,
                            "MSFT": 2.4076200973124618e-05
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.0006720380408552348,
                            "CSCO": 0.0010167394389176759,
                            "NFLX": 0.00032373217164410396,
                            "AMD": 0.00024632601562600326,
                            "CVX": 0.0005917242463493487,
                            "PFE": 0.0010879960385491486,
                            "MMM": 0.001040585213936048,
                            "MSFT": 0.0006605160493993175
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.0008478170535496692,
                            "CSCO": 0.0012826789302491511,
                            "NFLX": 0.00040840791624422823,
                            "AMD": 0.0003107553205096829,
                            "CVX": 0.0007464962941909862,
                            "PFE": 0.0013725734848321666,
                            "MMM": 0.0013127618325353915,
                            "MSFT": 0.0008332813572745761
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 0.0006192827496034944,
                            "CSCO": 0.0009369249314547161,
                            "NFLX": 0.00029831904922485977,
                            "AMD": 0.0002269893115895872,
                            "CVX": 0.0005452736244215329,
                            "PFE": 0.0010025878556710543,
                            "MMM": 0.0009588988023103166,
                            "MSFT": 0.0006086652397068107
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.00519850123867538,
                            "CSCO": 0.007864913756812489,
                            "NFLX": 0.00250420659692011,
                            "AMD": 0.001905436923957687,
                            "CVX": 0.004577239740308049,
                            "PFE": 0.008416113984967135,
                            "MMM": 0.008049371009875763,
                            "MSFT": 0.005109373714317729
                        }
                    }
                },
                "allocation": {
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.19291882414448006,
                        "Shares": 6781,
                        "Purchase Value": 192936.76050560738,
                        "Current Value": 193800.9794826097,
                        "Net Value": 864.2189770023106,
                        "Net Change": 0.004479286242484586,
                        "%Shares": 0.46270897304674174,
                        "%Purchase Value": 0.1929369898788389,
                        "%Current Value": 0.16189062010528674
                    },
                    "MMM": {
                        "Company Name": "3M Company",
                        "Sector": "Industrials",
                        "Industry": "Conglomerates",
                        "Market Cap": 74311114752,
                        "Volume (3 Months Average)": 4169252.3076923075,
                        "Current Price": 135.2700042725,
                        "Purchase Price": 89.3647994995,
                        "Price Diff": 45.905204772999994,
                        "Weight": 0.1845121386309221,
                        "Shares": 2065,
                        "Purchase Value": 184538.31096646748,
                        "Current Value": 279332.55882271245,
                        "Net Value": 94794.24785624497,
                        "Net Change": 0.5136832962206426,
                        "%Shares": 0.14090754008870693,
                        "%Purchase Value": 0.18453853035518644,
                        "%Current Value": 0.23333897116584615
                    },
                    "CSCO": {
                        "Company Name": "Cisco Systems, Inc.",
                        "Sector": "Technology",
                        "Industry": "Communication Equipment",
                        "Market Cap": 210511003648,
                        "Volume (3 Months Average)": 18805300.0,
                        "Current Price": 52.75,
                        "Purchase Price": 48.9177017212,
                        "Price Diff": 3.8322982788000033,
                        "Weight": 0.18028390735584074,
                        "Shares": 3685,
                        "Purchase Value": 180261.730842622,
                        "Current Value": 194383.75,
                        "Net Value": 14122.019157378003,
                        "Net Change": 0.07834174836425636,
                        "%Shares": 0.2514500170590242,
                        "%Purchase Value": 0.1802619451471206,
                        "%Current Value": 0.16237743436541727
                    },
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.11916292341931652,
                        "Shares": 644,
                        "Purchase Value": 119100.21185303641,
                        "Current Value": 146059.20196535919,
                        "Net Value": 26958.990112322776,
                        "Net Change": 0.2263555177012514,
                        "%Shares": 0.04394404640054589,
                        "%Purchase Value": 0.11910035344554784,
                        "%Current Value": 0.12200977952424179
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.1171198929626593,
                        "Shares": 317,
                        "Purchase Value": 116926.74826050301,
                        "Current Value": 131891.0192260762,
                        "Net Value": 14964.270965573189,
                        "Net Change": 0.1279798778995722,
                        "%Shares": 0.021630842715796655,
                        "%Purchase Value": 0.11692688726908815,
                        "%Current Value": 0.11017446323455625
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.10492202340710839,
                        "Shares": 725,
                        "Purchase Value": 104956.848144495,
                        "Current Value": 109286.50398257,
                        "Net Value": 4329.655838074992,
                        "Net Change": 0.04125177074786313,
                        "%Shares": 0.04947117024906175,
                        "%Purchase Value": 0.10495697292264182,
                        "%Current Value": 0.09129190134183372
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.05740281000894311,
                        "Shares": 123,
                        "Purchase Value": 57625.5,
                        "Current Value": 88523.101501461,
                        "Net Value": 30897.601501461002,
                        "Net Change": 0.5361793216798293,
                        "%Shares": 0.008393039918116683,
                        "%Purchase Value": 0.05762556850818433,
                        "%Current Value": 0.07394730322815901
                    },
                    "AMD": {
                        "Company Name": "Advanced Micro Devices, Inc.",
                        "Sector": "Technology",
                        "Industry": "Semiconductors",
                        "Market Cap": 276598226944,
                        "Volume (3 Months Average)": 46165160.0,
                        "Current Price": 170.8999938965,
                        "Purchase Price": 138.5800018311,
                        "Price Diff": 32.319992065400015,
                        "Weight": 0.04367748007072976,
                        "Shares": 315,
                        "Purchase Value": 43652.700576796495,
                        "Current Value": 53833.498077397504,
                        "Net Value": 10180.79750060101,
                        "Net Change": 0.2332226269183582,
                        "%Shares": 0.021494370522006142,
                        "%Purchase Value": 0.043652752473391884,
                        "%Current Value": 0.044969527034659174
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 1.1888504722874522
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.15516226590190704,
                    "Expected Daily Return": 0.00061572327738852,
                    "Expected Current Return": 0.11760314598120733,
                    "Net Value": 197111.80190865812,
                    "Net Change": 0.1971120362453955,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.024525782340269645,
                        "95.0% CVaR": 0.03281746310915763,
                        "99.0% CVaR": 0.05809105702443222,
                        "99.9% CVaR": 0.10808525806218999
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.0520940579452126,
                        "95.0% EVaR": 0.06301028662948027,
                        "99.0% EVaR": 0.0854954199192831,
                        "99.9% EVaR": 0.10896790779843009
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.239365966323138,
                        "95.0% CDaR": 0.2667825500085255,
                        "99.0% CDaR": 0.30636204194695843,
                        "99.9% CDaR": 0.3223567566762507
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.2634399457016672,
                        "95.0% EDaR": 0.28326279842154767,
                        "99.0% EDaR": 0.3121368365102636,
                        "99.9% EDaR": 0.32432536449293764
                    },
                    "VaR": {
                        "90.0% VaR": 0.013511185727048063,
                        "95.0% VaR": 0.019457060662399276,
                        "99.0% VaR": 0.03835358360599926,
                        "99.9% VaR": 0.09225668813549703
                    },
                    "DaR": {
                        "90.0% DaR": 0.19582426669362918,
                        "95.0% DaR": 0.23533240828855484,
                        "99.0% DaR": 0.28933997976095804,
                        "99.9% DaR": 0.3212793239430963
                    },
                    "ERM": {
                        "90.0% ERM": 2.3020697318947594,
                        "95.0% ERM": 2.9952169124547035,
                        "99.0% ERM": 4.6046548248888035,
                        "99.9% ERM": 6.907239917882849
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.0029225639228123773,
                            "CSCO": 0.0044216038712626875,
                            "NFLX": 0.0014078488239991905,
                            "AMD": 0.0010712243693861833,
                            "CVX": 0.002573294708783417,
                            "PFE": 0.004731485090308274,
                            "MMM": 0.0045253045511996545,
                            "MSFT": 0.0028724570025178606
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.0039106248432927955,
                            "CSCO": 0.005916460478825096,
                            "NFLX": 0.001883814599830475,
                            "AMD": 0.0014333840909221416,
                            "CVX": 0.003443274632500953,
                            "PFE": 0.006331106394423543,
                            "MMM": 0.0060552203027120655,
                            "MSFT": 0.0038435777666505624
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.0069223001795495655,
                            "CSCO": 0.0104728827427956,
                            "NFLX": 0.0033345899095921627,
                            "AMD": 0.0025372709854722644,
                            "CVX": 0.006095031244861146,
                            "PFE": 0.011206858414463403,
                            "MMM": 0.01071850516690884,
                            "MSFT": 0.0068036183807892395
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.01287975532922181,
                            "CSCO": 0.019486032651016,
                            "NFLX": 0.006204397533311479,
                            "AMD": 0.004720891704950986,
                            "CVX": 0.01134052397636445,
                            "PFE": 0.020851680892710375,
                            "MMM": 0.019943042119529793,
                            "MSFT": 0.0126589338550851
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.0062076802375268065,
                            "CSCO": 0.009391720316384508,
                            "NFLX": 0.0029903453108239123,
                            "AMD": 0.0022753371777054646,
                            "CVX": 0.0054658139670988575,
                            "PFE": 0.010049924403704825,
                            "MMM": 0.009611986041434357,
                            "MSFT": 0.006101250490533871
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.007508489960257941,
                            "CSCO": 0.011359740677174192,
                            "NFLX": 0.0036169675120011043,
                            "AMD": 0.0027521305385100944,
                            "CVX": 0.006611166768626938,
                            "PFE": 0.012155870405565988,
                            "MMM": 0.011626162741752802,
                            "MSFT": 0.0073797580255912125
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.01018788417654384,
                            "CSCO": 0.015413448364076736,
                            "NFLX": 0.004907677346261418,
                            "AMD": 0.0037342244996631598,
                            "CVX": 0.008970352449971582,
                            "PFE": 0.016493675880566654,
                            "MMM": 0.015774942772455662,
                            "MSFT": 0.010013214429744047
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.012984934452147467,
                            "CSCO": 0.019645160194291966,
                            "NFLX": 0.006255064108425312,
                            "AMD": 0.0047594436212150485,
                            "CVX": 0.011433133372650511,
                            "PFE": 0.02102196064195725,
                            "MMM": 0.02010590171002547,
                            "MSFT": 0.01276230969771706
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.028523548314154788,
                            "CSCO": 0.043153831696741904,
                            "NFLX": 0.013740279087454165,
                            "AMD": 0.01045490222368983,
                            "CVX": 0.025114761521421405,
                            "PFE": 0.046178200763266994,
                            "MMM": 0.04416592636173947,
                            "MSFT": 0.028034516354669435
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.031790588576275904,
                            "CSCO": 0.04809660052989197,
                            "NFLX": 0.015314068031840754,
                            "AMD": 0.01165238951121584,
                            "CVX": 0.02799136495660258,
                            "PFE": 0.05146737584991069,
                            "MMM": 0.04922461885148397,
                            "MSFT": 0.03124554370130381
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.03650699654311084,
                            "CSCO": 0.055232145987711645,
                            "NFLX": 0.017586042087833115,
                            "AMD": 0.013381121981566352,
                            "CVX": 0.03214412533620829,
                            "PFE": 0.0591030048949091,
                            "MMM": 0.05652751555496957,
                            "MSFT": 0.03588108956064951
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.03841297350951131,
                            "CSCO": 0.058115735656150476,
                            "NFLX": 0.018504183658585922,
                            "AMD": 0.014079730815392022,
                            "CVX": 0.03382232316942512,
                            "PFE": 0.06218868645301055,
                            "MMM": 0.05947873457646279,
                            "MSFT": 0.03775438883771249
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.03139227407523667,
                            "CSCO": 0.04749398276470708,
                            "NFLX": 0.01512219315187909,
                            "AMD": 0.011506392978218698,
                            "CVX": 0.02764065214927769,
                            "PFE": 0.0508225245574513,
                            "MMM": 0.04860786778222861,
                            "MSFT": 0.03085405824266804
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.03375442315584817,
                            "CSCO": 0.05106772410798649,
                            "NFLX": 0.01626008060039365,
                            "AMD": 0.01237220523283629,
                            "CVX": 0.02972050596634865,
                            "PFE": 0.05464672599535986,
                            "MMM": 0.05226542473133955,
                            "MSFT": 0.033175708631435
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.03719513794542026,
                            "CSCO": 0.05627324851576156,
                            "NFLX": 0.017917531522991196,
                            "AMD": 0.01363335045601767,
                            "CVX": 0.03275002846655064,
                            "PFE": 0.06021707147173786,
                            "MMM": 0.05759303524999922,
                            "MSFT": 0.03655743288178516
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.038647558572013845,
                            "CSCO": 0.05847064396539405,
                            "NFLX": 0.018617187279069324,
                            "AMD": 0.01416571464407245,
                            "CVX": 0.03402887348484696,
                            "PFE": 0.06256846795820743,
                            "MMM": 0.059841966614845254,
                            "MSFT": 0.03798495197448832
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.0016100323900963907,
                            "CSCO": 0.0024358493558826904,
                            "NFLX": 0.0007755800272852838,
                            "AMD": 0.0005901345453250701,
                            "CVX": 0.0014176209451111257,
                            "PFE": 0.0026065620632597943,
                            "MMM": 0.0024929777739372285,
                            "MSFT": 0.0015824286261504792
                        },
                        "95.0% VaR": {
                            "AAPL": 0.002318560229678481,
                            "CSCO": 0.0035077949218769644,
                            "NFLX": 0.0011168899565361864,
                            "AMD": 0.0008498353793169244,
                            "CVX": 0.0020414741742537847,
                            "PFE": 0.0037536332642978867,
                            "MMM": 0.0035900638742908763,
                            "MSFT": 0.002278808862148172
                        },
                        "99.0% VaR": {
                            "AAPL": 0.0045703251460980435,
                            "CSCO": 0.006914533913588463,
                            "NFLX": 0.0022016034728972907,
                            "AMD": 0.0016751878835921004,
                            "CVX": 0.004024135596855143,
                            "PFE": 0.007399128250996385,
                            "MMM": 0.007076701735302797,
                            "MSFT": 0.004491967606669038
                        },
                        "99.9% VaR": {
                            "AAPL": 0.010993576663209999,
                            "CSCO": 0.01663239621677664,
                            "NFLX": 0.005295793141096252,
                            "AMD": 0.004029539657429702,
                            "CVX": 0.009679758392014919,
                            "PFE": 0.01779805179456409,
                            "MMM": 0.017022478830886575,
                            "MSFT": 0.010805093439518854
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.02333499209565675,
                            "CSCO": 0.03530396395461969,
                            "NFLX": 0.011240863176155002,
                            "AMD": 0.008553110505876258,
                            "CVX": 0.020546278293708798,
                            "PFE": 0.03777818726949001,
                            "MMM": 0.03613195424347357,
                            "MSFT": 0.022934917154649098
                        },
                        "95.0% DaR": {
                            "AAPL": 0.028042897746972387,
                            "CSCO": 0.04242664609372071,
                            "NFLX": 0.013508741521934943,
                            "AMD": 0.010278726573020192,
                            "CVX": 0.02469155245090294,
                            "PFE": 0.045400051490116694,
                            "MMM": 0.0434216859424866,
                            "MSFT": 0.02756210646940038
                        },
                        "99.0% DaR": {
                            "AAPL": 0.03447859785040163,
                            "CSCO": 0.05216334210556539,
                            "NFLX": 0.01660892788620972,
                            "AMD": 0.012637641199674598,
                            "CVX": 0.03035813612909151,
                            "PFE": 0.055819128673471684,
                            "MMM": 0.053386738457122086,
                            "MSFT": 0.033887467459421415
                        },
                        "99.9% DaR": {
                            "AAPL": 0.03828458347524096,
                            "CSCO": 0.05792149187310432,
                            "NFLX": 0.01844233599210724,
                            "AMD": 0.014032671268662119,
                            "CVX": 0.033709276746977504,
                            "PFE": 0.06198082939703563,
                            "MMM": 0.05927993515863751,
                            "MSFT": 0.03762820003133098
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 0.27432135916770173,
                            "CSCO": 0.4150261262715999,
                            "NFLX": 0.13214527144729346,
                            "AMD": 0.10054860483626356,
                            "CVX": 0.24153781429465768,
                            "PFE": 0.4441125857757354,
                            "MMM": 0.42475980950941555,
                            "MSFT": 0.26961816059209204
                        },
                        "95.0% ERM": {
                            "AAPL": 0.3569188035630815,
                            "CSCO": 0.5399894083556311,
                            "NFLX": 0.17193386736121052,
                            "AMD": 0.13082352700125302,
                            "CVX": 0.3142642189979393,
                            "PFE": 0.5778337248084214,
                            "MMM": 0.5526538781805247,
                            "MSFT": 0.35079948418664175
                        },
                        "99.0% ERM": {
                            "AAPL": 0.5487041302706108,
                            "CSCO": 0.8301451638558781,
                            "NFLX": 0.26432012606985517,
                            "AMD": 0.20111971934667036,
                            "CVX": 0.48312970131863764,
                            "PFE": 0.8883245944087547,
                            "MMM": 0.8496147093974273,
                            "MSFT": 0.5392966802209693
                        },
                        "99.9% ERM": {
                            "AAPL": 0.82308690137352,
                            "CSCO": 1.2452642014401567,
                            "NFLX": 0.396494980692417,
                            "AMD": 0.30169083385707723,
                            "CVX": 0.7247215883426178,
                            "PFE": 1.3325366030417742,
                            "MMM": 1.2744696092854393,
                            "MSFT": 0.808975199849847
                        }
                    }
                }
            }
        },
        {
            "name": "Max Information",
            "error": False,
            "messages": None,
            "stacktraces": None,
            "data": {
                "performance": {
                    "annual_expected_return": 0.09205092785807487,
                    "annual_standard_deviation": 0.21399930198104009,
                    "annual_sharpe_ratio": 0.43014592573872223,
                    "annual_sortino_ratio": 0.6013638750678735,
                    "cvar_900": -0.023553727404121906,
                    "cvar_950": -0.030652650794350592,
                    "cvar_990": -0.05523921879885278,
                    "cvar_999": -0.09612509024538038,
                    "annual_tracking_error": [
                        {
                            "index": "^GSPC",
                            "value": 0.1209945784369023
                        }
                    ]
                },
                "weights": [
                    0.03402351211843328,
                    0.13933009474240643,
                    0.07524674601471112,
                    1.273375657931062e-07,
                    0.07117100501968873,
                    0.3439058333860824,
                    0.25668007798735504,
                    0.07964260339375719
                ],
                "position": [
                    0.21399930198104009,
                    0.09205092785807487
                ],
                "summary": {
                    "stats_descriptive": {
                        "daily_mean_return": 0.0003652814597542653,
                        "annual_mean_return": 0.09205092785807487,
                        "daily_variance": 0.0001817289732078269,
                        "annual_variance": 0.04579570124837238,
                        "daily_standard_deviation": 0.013480688899601048,
                        "annual_standard_deviation": 0.21399930198104009,
                        "daily_semi_variance": 9.297819880335465e-05,
                        "annual_semi_variance": 0.023430506098445374,
                        "daily_semi_deviation": 0.009642520355350808,
                        "annual_semi_deviation": 0.15307026523281841,
                        "mean_absolute_deviation": 0.009203931091071135
                    },
                    "stats_moments": {
                        "skew": -0.10042988710723874,
                        "kurtosis": 12.36209694737223,
                        "first_lower_partial_moment": 0.004601965545535568,
                        "fourth_central_moment": 4.0826344009825774e-07,
                        "fourth_lower_partial_moment": 2.1411989028030773e-07
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": 0.01910810039044089,
                        "conditional_var_at_95": 0.030652650794350592,
                        "entropic_var_at_95": 0.05715386803512479,
                        "drawdown_at_risk_at_95": 0.27633717286400444,
                        "conditional_dar_at_95": 0.2960167591971722,
                        "entropic_dar_at_95": 0.3086319646145728,
                        "entropic_risk_measure_at_95": 2.9954578254928172,
                        "worst_realization": 0.09686187096230882,
                        "average_drawdown": 0.11369506573613476,
                        "max_drawdown": 0.33937099622104716,
                        "ulcer_index": 0.15310457160898464,
                        "gini_mean_difference": 0.01363431514456305
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": 0.027096646356483726,
                        "annual_sharpe_ratio": 0.43014592573872223,
                        "daily_sortino_ratio": 0.037882363354469255,
                        "annual_sortino_ratio": 0.6013638750678735,
                        "mean_absolute_deviation_ratio": 0.03968754830298872,
                        "calmar_ratio": 0.0010763484912433164,
                        "value_at_risk_ratio_at_95": 0.01911657633623292,
                        "conditional_var_ratio_at_95": 0.011916798393879468,
                        "entropic_var_ratio_at_95": 0.006391194022594866,
                        "drawdown_at_risk_ratio_at_95": 0.0013218687010814632,
                        "conditional_dar_ratio_at_95": 0.0012339891185382413,
                        "entropic_dar_ratio_at_95": 0.0011835503176426906,
                        "entropic_risk_measure_ratio_at_95": 0.00012194511858772997,
                        "worst_realization_ratio": 0.003771158414815307,
                        "average_drawdown_ratio": 0.0032128171736319332,
                        "ulcer_index_ratio": 0.0023858298672306236,
                        "gini_mean_difference_ratio": 0.026791331715691525
                    }
                },
                "symbol_contribution_summary": {
                    "stats_descriptive": {
                        "daily_mean_return": {
                            "AAPL": 1.2428159755159856e-05,
                            "CSCO": 5.08947068760144e-05,
                            "NFLX": 2.7486244726043623e-05,
                            "CVX": 2.599745191622229e-05,
                            "PFE": 0.00012562244083373116,
                            "MMM": 9.37604855162917e-05,
                            "MSFT": 2.9091970130802294e-05
                        },
                        "annual_mean_return": {
                            "AAPL": 0.003131896258300284,
                            "CSCO": 0.012825466132755628,
                            "NFLX": 0.006926533670962994,
                            "CVX": 0.006551357882888018,
                            "PFE": 0.03165685509010025,
                            "MMM": 0.02362764235010551,
                            "MSFT": 0.007331176472962178
                        },
                        "daily_variance": {
                            "AAPL": 6.1830587095425815e-06,
                            "CSCO": 2.532031827871446e-05,
                            "NFLX": 1.3674515631763129e-05,
                            "CVX": 1.2933835311360235e-05,
                            "PFE": 6.249766193973489e-05,
                            "MMM": 4.664621295536217e-05,
                            "MSFT": 1.4473370381349438e-05
                        },
                        "annual_variance": {
                            "AAPL": 0.0015581307948047305,
                            "CSCO": 0.006380720206236043,
                            "NFLX": 0.0034459779392043083,
                            "CVX": 0.0032593264984627788,
                            "PFE": 0.015749410808813192,
                            "MMM": 0.011754845664751268,
                            "MSFT": 0.003647289336100058
                        },
                        "daily_standard_deviation": {
                            "AAPL": 0.0004586604405451093,
                            "CSCO": 0.0018782659007481285,
                            "NFLX": 0.0010143781029000542,
                            "CVX": 0.0009594342995143967,
                            "PFE": 0.004636088140983987,
                            "MMM": 0.003460224718689461,
                            "MSFT": 0.0010736372962199111
                        },
                        "annual_standard_deviation": {
                            "AAPL": 0.007281008771434114,
                            "CSCO": 0.029816546816593653,
                            "NFLX": 0.016102753173978183,
                            "CVX": 0.015230547334923314,
                            "PFE": 0.0735956176633163,
                            "MMM": 0.05492936451630447,
                            "MSFT": 0.017043463704490034
                        },
                        "daily_semi_variance": {
                            "AAPL": 3.163445276561457e-06,
                            "CSCO": 1.2954662897864944e-05,
                            "NFLX": 6.996307801154151e-06,
                            "CVX": 6.617352696392756e-06,
                            "PFE": 3.1975749017918576e-05,
                            "MMM": 2.3865654358963203e-05,
                            "MSFT": 7.405026754499565e-06
                        },
                        "annual_semi_variance": {
                            "AAPL": 0.0007971882096934872,
                            "CSCO": 0.003264575050261966,
                            "NFLX": 0.001763069565890846,
                            "CVX": 0.0016675728794909746,
                            "PFE": 0.008057888752515481,
                            "MMM": 0.0060141448984587275,
                            "MSFT": 0.0018660667421338906
                        },
                        "daily_semi_deviation": {
                            "AAPL": 0.00032807244993846496,
                            "CSCO": 0.0013434934457437957,
                            "NFLX": 0.0007255683725128747,
                            "CVX": 0.0006862679520008136,
                            "PFE": 0.0033161194210157576,
                            "MMM": 0.002475043191972079,
                            "MSFT": 0.0007679555221670218
                        },
                        "annual_semi_deviation": {
                            "AAPL": 0.005207988687293196,
                            "CSCO": 0.021327297272899993,
                            "NFLX": 0.011518040837057637,
                            "CVX": 0.010894166002486586,
                            "PFE": 0.05264176383479515,
                            "MMM": 0.0392900926206097,
                            "MSFT": 0.012190915977676143
                        },
                        "mean_absolute_deviation": {
                            "AAPL": 0.0003131501008900552,
                            "CSCO": 0.0012823847542172745,
                            "NFLX": 0.0006925659533363954,
                            "CVX": 0.0006550531092963614,
                            "PFE": 0.003165285995362707,
                            "MMM": 0.0023624660510770568,
                            "MSFT": 0.0007330251268912847
                        }
                    },
                    "stats_moments": {
                        "skew": {
                            "AAPL": -0.0034169779161556738,
                            "CSCO": -0.013992907467443532,
                            "NFLX": -0.007557023169737441,
                            "CVX": -0.007147696909606387,
                            "PFE": -0.03453842842052451,
                            "MMM": -0.025778354537500218,
                            "MSFT": -0.007998498686270976
                        },
                        "kurtosis": {
                            "AAPL": 0.4206020088566021,
                            "CSCO": 1.7224123582199833,
                            "NFLX": 0.9302076876585366,
                            "CVX": 0.8798229759298238,
                            "PFE": 4.251397794448238,
                            "MMM": 3.1731044125941392,
                            "MSFT": 0.9845497096649064
                        },
                        "first_lower_partial_moment": {
                            "AAPL": 0.0001565750504450276,
                            "CSCO": 0.0006411923771086372,
                            "NFLX": 0.0003462829766681977,
                            "CVX": 0.0003275265546481807,
                            "PFE": 0.0015826429976813535,
                            "MMM": 0.0011812330255385284,
                            "MSFT": 0.00036651256344564235
                        },
                        "fourth_central_moment": {
                            "AAPL": 1.3890557870486159e-08,
                            "CSCO": 5.688339103214357e-08,
                            "NFLX": 3.072049929603943e-08,
                            "CVX": 2.905652304457541e-08,
                            "PFE": 1.4040419648678884e-07,
                            "MMM": 1.0479310498790555e-07,
                            "MSFT": 3.2515167380318753e-08
                        },
                        "fourth_lower_partial_moment": {
                            "AAPL": 7.285111609418033e-09,
                            "CSCO": 2.983334839789491e-08,
                            "NFLX": 1.6111827052260967e-08,
                            "CVX": 1.5239129726468666e-08,
                            "PFE": 7.363708868815338e-08,
                            "MMM": 5.496031713430629e-08,
                            "MSFT": 1.705306767180548e-08
                        }
                    },
                    "stats_risk_measures": {
                        "value_at_risk_at_95": {
                            "AAPL": 0.0006501247679797108,
                            "CSCO": 0.0026623337767626453,
                            "NFLX": 0.001437822559991933,
                            "CVX": 0.0013599428819766012,
                            "PFE": 0.006571388025984055,
                            "MMM": 0.004904669322957229,
                            "MSFT": 0.0015218190547887148
                        },
                        "conditional_var_at_95": {
                            "AAPL": 0.001042910968565435,
                            "CSCO": 0.004270837283120792,
                            "NFLX": 0.0023065125227058223,
                            "CVX": 0.0021815802413486093,
                            "PFE": 0.010541626759268792,
                            "MMM": 0.007867925798295589,
                            "MSFT": 0.0024412572210455526
                        },
                        "entropic_var_at_95": {
                            "AAPL": 0.0019445755693259243,
                            "CSCO": 0.007963254862250422,
                            "NFLX": 0.004300643139430781,
                            "CVX": 0.004067698746793351,
                            "PFE": 0.019655551120747797,
                            "MMM": 0.014670261172610175,
                            "MSFT": 0.004551883423966335
                        },
                        "drawdown_at_risk_at_95": {
                            "AAPL": 0.009401962346935046,
                            "CSCO": 0.038502089378752824,
                            "NFLX": 0.020793475708711647,
                            "CVX": 0.019667196821403624,
                            "PFE": 0.09503397783074476,
                            "MMM": 0.07093025611362402,
                            "MSFT": 0.02200821466383251
                        },
                        "conditional_dar_at_95": {
                            "AAPL": 0.010071531076288585,
                            "CSCO": 0.04124404835619883,
                            "NFLX": 0.022274300731762755,
                            "CVX": 0.02106781293745795,
                            "PFE": 0.10180190323115731,
                            "MMM": 0.07598161451160809,
                            "MSFT": 0.02357554835269865
                        },
                        "entropic_dar_at_95": {
                            "AAPL": 0.010500744725339062,
                            "CSCO": 0.04300172634601862,
                            "NFLX": 0.02322355401060491,
                            "CVX": 0.02196564989987255,
                            "PFE": 0.10614034651601191,
                            "MMM": 0.07921968683430124,
                            "MSFT": 0.024580256282424526
                        },
                        "entropic_risk_measure_at_95": {
                            "AAPL": 0.10191600860364712,
                            "CSCO": 0.417357475768082,
                            "NFLX": 0.22539848289433104,
                            "CVX": 0.2131897710814817,
                            "PFE": 1.0301555510264697,
                            "MMM": 0.7688744461619296,
                            "MSFT": 0.23856608995687595
                        },
                        "worst_realization": {
                            "AAPL": 0.003295581460151556,
                            "CSCO": 0.01349577537662442,
                            "NFLX": 0.0072885415309157115,
                            "CVX": 0.006893757582309233,
                            "PFE": 0.033311366698416334,
                            "MMM": 0.024862515758538782,
                            "MSFT": 0.007714332555352777
                        },
                        "average_drawdown": {
                            "AAPL": 0.0038683059394601115,
                            "CSCO": 0.015841146297932793,
                            "NFLX": 0.008555184823969228,
                            "CVX": 0.008091793124609527,
                            "PFE": 0.03910040131282077,
                            "MMM": 0.02918326205605408,
                            "MSFT": 0.00905497218128825
                        },
                        "max_drawdown": {
                            "AAPL": 0.011546594672886832,
                            "CSCO": 0.047284599077409104,
                            "NFLX": 0.02553656640916883,
                            "CVX": 0.02415337795121727,
                            "PFE": 0.11671168014424549,
                            "MMM": 0.08710978486901272,
                            "MSFT": 0.027028393097106914
                        },
                        "ulcer_index": {
                            "AAPL": 0.005209155910847058,
                            "CSCO": 0.021332077184150162,
                            "NFLX": 0.011520622280560416,
                            "CVX": 0.010896607622067829,
                            "PFE": 0.052653561999183404,
                            "MMM": 0.03929889838504082,
                            "MSFT": 0.012193648227134944
                        },
                        "gini_mean_difference": {
                            "AAPL": 0.00046388734561786474,
                            "CSCO": 0.0018996706627392348,
                            "NFLX": 0.0010259379794079102,
                            "CVX": 0.0009703680351580185,
                            "PFE": 0.00468892110951524,
                            "MMM": 0.003499657520248489,
                            "MSFT": 0.0010858724918762922
                        }
                    },
                    "stats_ratios": {
                        "daily_sharpe_ratio": {
                            "AAPL": 0.0009219231930741804,
                            "CSCO": 0.0037753787847979044,
                            "NFLX": 0.0020389347258697632,
                            "CVX": 0.0019284957994239946,
                            "PFE": 0.009318695933814545,
                            "MMM": 0.0069551701856324635,
                            "MSFT": 0.0021580477338708744
                        },
                        "annual_sharpe_ratio": {
                            "AAPL": 0.014635076980661197,
                            "CSCO": 0.05993228021786697,
                            "NFLX": 0.03236708534487028,
                            "CVX": 0.03061392173825153,
                            "PFE": 0.14792971190581258,
                            "MMM": 0.11040990382388664,
                            "MSFT": 0.03425794572737301
                        },
                        "daily_sortino_ratio": {
                            "AAPL": 0.0012888912127899472,
                            "CSCO": 0.005278153947351743,
                            "NFLX": 0.002850524936749655,
                            "CVX": 0.0026961262157767533,
                            "PFE": 0.013027967399002792,
                            "MMM": 0.009723649218356311,
                            "MSFT": 0.003017050424442053
                        },
                        "annual_sortino_ratio": {
                            "AAPL": 0.0204605136963518,
                            "CSCO": 0.08378809635723972,
                            "NFLX": 0.04525068053176626,
                            "CVX": 0.042799676821121756,
                            "PFE": 0.2068125709585103,
                            "MMM": 0.15435814600679035,
                            "MSFT": 0.047894190696093256
                        },
                        "mean_absolute_deviation_ratio": {
                            "AAPL": 0.0013503099525828254,
                            "CSCO": 0.0055296705692840405,
                            "NFLX": 0.002986359247377289,
                            "CVX": 0.0028246030591692274,
                            "PFE": 0.013648781112192298,
                            "MMM": 0.010187004290726394,
                            "MSFT": 0.003160820071656646
                        },
                        "calmar_ratio": {
                            "AAPL": 3.66211605987238e-05,
                            "CSCO": 0.00014996775635730655,
                            "NFLX": 8.099173185719334e-05,
                            "CVX": 7.660481362788296e-05,
                            "PFE": 0.00037016257203048596,
                            "MMM": 0.00027627724985437884,
                            "MSFT": 8.572320691734488e-05
                        },
                        "value_at_risk_ratio_at_95": {
                            "AAPL": 0.0006504131494608029,
                            "CSCO": 0.00266351473124326,
                            "NFLX": 0.0014384603474133946,
                            "CVX": 0.0013605461236339276,
                            "PFE": 0.006574302953556578,
                            "MMM": 0.00490684492966118,
                            "MSFT": 0.001522494101263775
                        },
                        "conditional_var_ratio_at_95": {
                            "AAPL": 0.0004054513861962769,
                            "CSCO": 0.0016603688606727123,
                            "NFLX": 0.0008967004162364141,
                            "CVX": 0.0008481306263083037,
                            "PFE": 0.004098257004803117,
                            "MMM": 0.0030588051306013686,
                            "MSFT": 0.0009490849690612749
                        },
                        "entropic_var_ratio_at_95": {
                            "AAPL": 0.00021745089496868244,
                            "CSCO": 0.0008904857820775363,
                            "NFLX": 0.0004809166145876869,
                            "CVX": 0.00045486775978565715,
                            "PFE": 0.0021979691865566817,
                            "MMM": 0.001640492389048275,
                            "MSFT": 0.0005090113955703466
                        },
                        "drawdown_at_risk_ratio_at_95": {
                            "AAPL": 4.497462149718165e-05,
                            "CSCO": 0.00018417611481124014,
                            "NFLX": 9.946633108087344e-05,
                            "CVX": 9.407873593979548e-05,
                            "PFE": 0.0004545984151598544,
                            "MMM": 0.00033929740448793925,
                            "MSFT": 0.00010527707810457881
                        },
                        "conditional_dar_ratio_at_95": {
                            "AAPL": 4.198464907482367e-05,
                            "CSCO": 0.0001719318426904141,
                            "NFLX": 9.285367761132558e-05,
                            "CVX": 8.782425693305355e-05,
                            "PFE": 0.00042437611023927194,
                            "MMM": 0.00031674046351490287,
                            "MSFT": 9.827811847444955e-05
                        },
                        "entropic_dar_ratio_at_95": {
                            "AAPL": 4.026854370278998e-05,
                            "CSCO": 0.0001649041988880606,
                            "NFLX": 8.905832148776009e-05,
                            "CVX": 8.423447632421531e-05,
                            "PFE": 0.00040702991017347,
                            "MMM": 0.000303793826518851,
                            "MSFT": 9.42610405475436e-05
                        },
                        "entropic_risk_measure_ratio_at_95": {
                            "AAPL": 4.149001748377197e-06,
                            "CSCO": 1.69906270897475e-05,
                            "NFLX": 9.175974534551006e-06,
                            "CVX": 8.678957752291221e-06,
                            "PFE": 4.193764297551529e-05,
                            "MMM": 3.130088653505448e-05,
                            "MSFT": 9.712027952193263e-06
                        },
                        "worst_realization_ratio": {
                            "AAPL": 0.0001283080703654376,
                            "CSCO": 0.0005254359261325718,
                            "NFLX": 0.0002837674355551025,
                            "CVX": 0.0002683971686479038,
                            "PFE": 0.0012969235426250824,
                            "MMM": 0.0009679813592778532,
                            "MSFT": 0.0003003449122113556
                        },
                        "average_drawdown_ratio": {
                            "AAPL": 0.00010931133796081634,
                            "CSCO": 0.00044764217819383306,
                            "NFLX": 0.00024175406864035875,
                            "CVX": 0.00022865945630883906,
                            "PFE": 0.0011049067083111384,
                            "MMM": 0.0008246662676979533,
                            "MSFT": 0.0002558771565189942
                        },
                        "ulcer_index_ratio": {
                            "AAPL": 8.117432173678173e-05,
                            "CSCO": 0.00033241794376979755,
                            "NFLX": 0.00017952595691421306,
                            "CVX": 0.00016980193107895858,
                            "PFE": 0.0008205009132879429,
                            "MMM": 0.0006123950743662154,
                            "MSFT": 0.00019001372607671427
                        },
                        "gini_mean_difference_ratio": {
                            "AAPL": 0.0009115353153704847,
                            "CSCO": 0.0037328392615532035,
                            "NFLX": 0.002015960789714055,
                            "CVX": 0.0019067662468246,
                            "PFE": 0.00921369643445755,
                            "MMM": 0.0068768019898440245,
                            "MSFT": 0.0021337316779276062
                        }
                    }
                },
                "allocation": {
                    "PFE": {
                        "Company Name": "Pfizer Inc.",
                        "Sector": "Healthcare",
                        "Industry": "Drug Manufacturers - General",
                        "Market Cap": 161954283520,
                        "Volume (3 Months Average)": 31410904.615384616,
                        "Current Price": 28.5799999237,
                        "Purchase Price": 28.4525527954,
                        "Price Diff": 0.12744712830000182,
                        "Weight": 0.3439058333860824,
                        "Shares": 12088,
                        "Purchase Value": 343934.4581907952,
                        "Current Value": 345475.0390776856,
                        "Net Value": 1540.5808868904132,
                        "Net Change": 0.00447928624248457,
                        "%Shares": 0.6408312569580661,
                        "%Purchase Value": 0.34394065520783346,
                        "%Current Value": 0.28661576678642176
                    },
                    "MMM": {
                        "Company Name": "3M Company",
                        "Sector": "Industrials",
                        "Industry": "Conglomerates",
                        "Market Cap": 74311114752,
                        "Volume (3 Months Average)": 4169252.3076923075,
                        "Current Price": 135.2700042725,
                        "Purchase Price": 89.3647994995,
                        "Price Diff": 45.905204772999994,
                        "Weight": 0.25668007798735504,
                        "Shares": 2873,
                        "Purchase Value": 256745.0689620635,
                        "Current Value": 388630.72227489244,
                        "Net Value": 131885.65331282894,
                        "Net Change": 0.5136832962206425,
                        "%Shares": 0.15230875258442453,
                        "%Purchase Value": 0.25674969499917305,
                        "%Current Value": 0.32241893005917543
                    },
                    "CSCO": {
                        "Company Name": "Cisco Systems, Inc.",
                        "Sector": "Technology",
                        "Industry": "Communication Equipment",
                        "Market Cap": 210511003648,
                        "Volume (3 Months Average)": 18805300.0,
                        "Current Price": 52.75,
                        "Purchase Price": 48.9177017212,
                        "Price Diff": 3.8322982788000033,
                        "Weight": 0.13933009474240643,
                        "Shares": 2850,
                        "Purchase Value": 139415.44990541998,
                        "Current Value": 150337.5,
                        "Net Value": 10922.050094580016,
                        "Net Change": 0.07834174836425647,
                        "%Shares": 0.15108943434236335,
                        "%Purchase Value": 0.13941796189541658,
                        "%Current Value": 0.12472419991409106
                    },
                    "MSFT": {
                        "Company Name": "Microsoft Corporation",
                        "Sector": "Technology",
                        "Industry": "Software - Infrastructure",
                        "Market Cap": 3092590624768,
                        "Volume (3 Months Average)": 19942235.384615384,
                        "Current Price": 416.0599975586,
                        "Purchase Price": 368.854095459,
                        "Price Diff": 47.205902099599996,
                        "Weight": 0.07964260339375719,
                        "Shares": 216,
                        "Purchase Value": 79672.484619144,
                        "Current Value": 89868.9594726576,
                        "Net Value": 10196.474853513602,
                        "Net Change": 0.12797987789957233,
                        "%Shares": 0.011450988708052803,
                        "%Purchase Value": 0.07967392015935496,
                        "%Current Value": 0.07455780538680698
                    },
                    "NFLX": {
                        "Company Name": "Netflix, Inc.",
                        "Sector": "Communication Services",
                        "Industry": "Entertainment",
                        "Market Cap": 308870053888,
                        "Volume (3 Months Average)": 3144064.6153846155,
                        "Current Price": 719.700012207,
                        "Purchase Price": 468.5,
                        "Price Diff": 251.200012207,
                        "Weight": 0.07524674601471112,
                        "Shares": 160,
                        "Purchase Value": 74960.0,
                        "Current Value": 115152.00195312,
                        "Net Value": 40192.001953119994,
                        "Net Change": 0.5361793216798292,
                        "%Shares": 0.008482213857816891,
                        "%Purchase Value": 0.07496135063058128,
                        "%Current Value": 0.09553332543183665
                    },
                    "CVX": {
                        "Company Name": "Chevron Corporation",
                        "Sector": "Energy",
                        "Industry": "Oil & Gas Integrated",
                        "Market Cap": 273555423232,
                        "Volume (3 Months Average)": 7463387.692307692,
                        "Current Price": 150.7400054932,
                        "Purchase Price": 144.7680664062,
                        "Price Diff": 5.971939086999981,
                        "Weight": 0.07117100501968873,
                        "Shares": 492,
                        "Purchase Value": 71225.8886718504,
                        "Current Value": 74164.0827026544,
                        "Net Value": 2938.194030803992,
                        "Net Change": 0.0412517707478631,
                        "%Shares": 0.02608280761278694,
                        "%Purchase Value": 0.07122717202114895,
                        "%Current Value": 0.061528599833381895
                    },
                    "AAPL": {
                        "Company Name": "Apple Inc.",
                        "Sector": "Technology",
                        "Industry": "Consumer Electronics",
                        "Market Cap": 3448289886208,
                        "Volume (3 Months Average)": 54146816.92307692,
                        "Current Price": 226.8000030518,
                        "Purchase Price": 184.9382171631,
                        "Price Diff": 41.861785888699984,
                        "Weight": 0.03402351211843328,
                        "Shares": 184,
                        "Purchase Value": 34028.6319580104,
                        "Current Value": 41731.2005615312,
                        "Net Value": 7702.568603520798,
                        "Net Change": 0.22635551770125156,
                        "%Shares": 0.009754545936489424,
                        "%Purchase Value": 0.03402924508649175,
                        "%Current Value": 0.034621372588286
                    },
                    "Investment Amount": 1000000,
                    "Leftover": 18.017692716478088
                },
                "allocation_summary": {
                    "Expected Annual Return": 0.09205092785807487,
                    "Expected Daily Return": 0.0003652814597542653,
                    "Expected Current Return": 0.06976875881306467,
                    "Net Value": 205377.52373525803,
                    "Net Change": 0.205381224231046,
                    "Start Date": "2019-10-01",
                    "Purchase Date": "2024-01-02",
                    "Current Date": "2024-10-04"
                },
                "extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": 0.023553727404121906,
                        "95.0% CVaR": 0.030652650794350592,
                        "99.0% CVaR": 0.05523921879885278,
                        "99.9% CVaR": 0.09612509024538038
                    },
                    "EVaR": {
                        "90.0% EVaR": 0.04744150956785318,
                        "95.0% EVaR": 0.05715386803512479,
                        "99.0% EVaR": 0.07701814310116273,
                        "99.9% EVaR": 0.09672045668666773
                    },
                    "CDaR": {
                        "90.0% CDaR": 0.2823604419432694,
                        "95.0% CDaR": 0.2960167591971722,
                        "99.0% CDaR": 0.32208471650259257,
                        "99.9% CDaR": 0.33920591947089535
                    },
                    "EDaR": {
                        "90.0% EDaR": 0.29535309287776945,
                        "95.0% EDaR": 0.3086319646145728,
                        "99.0% EDaR": 0.3290640438107235,
                        "99.9% EDaR": 0.3409865578377052
                    },
                    "VaR": {
                        "90.0% VaR": 0.014099826692063834,
                        "95.0% VaR": 0.01910810039044089,
                        "99.0% VaR": 0.034303023541205215,
                        "99.9% VaR": 0.08544710884062037
                    },
                    "DaR": {
                        "90.0% DaR": 0.2620943676727026,
                        "95.0% DaR": 0.27633717286400444,
                        "99.0% DaR": 0.3088629085484494,
                        "99.9% DaR": 0.33681350280202793
                    },
                    "ERM": {
                        "90.0% ERM": 2.302310644932873,
                        "95.0% ERM": 2.9954578254928172,
                        "99.0% ERM": 4.604895737926918,
                        "99.9% ERM": 6.907480830920964
                    }
                },
                "ticker_contribution_extra_measures": {
                    "CVaR": {
                        "90.0% CVaR": {
                            "AAPL": 0.0008013806318142747,
                            "CSCO": 0.0032817434886423477,
                            "NFLX": 0.0017723415693633635,
                            "CVX": 0.0016763426647725347,
                            "PFE": 0.008100265283731214,
                            "MMM": 0.006045773356836975,
                            "MSFT": 0.001875880408961196
                        },
                        "95.0% CVaR": {
                            "AAPL": 0.001042910968565435,
                            "CSCO": 0.004270837283120792,
                            "NFLX": 0.0023065125227058223,
                            "CVX": 0.0021815802413486093,
                            "PFE": 0.010541626759268792,
                            "MMM": 0.007867925798295589,
                            "MSFT": 0.0024412572210455526
                        },
                        "99.0% CVaR": {
                            "AAPL": 0.0018794324695379108,
                            "CSCO": 0.0076964865687925415,
                            "NFLX": 0.004156571996296092,
                            "CVX": 0.0039314312190357175,
                            "PFE": 0.018997091995659066,
                            "MMM": 0.014178808794745097,
                            "MSFT": 0.004399395754786355
                        },
                        "99.9% CVaR": {
                            "AAPL": 0.0032705135893084315,
                            "CSCO": 0.01339311963645847,
                            "NFLX": 0.00723310117238082,
                            "CVX": 0.006841320151529055,
                            "PFE": 0.033057983479673064,
                            "MMM": 0.02467339880257632,
                            "MSFT": 0.007655653413454218
                        }
                    },
                    "EVaR": {
                        "90.0% EVaR": {
                            "AAPL": 0.0016141269812376218,
                            "CSCO": 0.006610030864517005,
                            "NFLX": 0.0035698196755788838,
                            "CVX": 0.0033764603455455314,
                            "PFE": 0.01631541396259145,
                            "MMM": 0.012177291926341116,
                            "MSFT": 0.003778365812041573
                        },
                        "95.0% EVaR": {
                            "AAPL": 0.0019445755693259243,
                            "CSCO": 0.007963254862250422,
                            "NFLX": 0.004300643139430781,
                            "CVX": 0.004067698746793351,
                            "PFE": 0.019655551120747797,
                            "MMM": 0.014670261172610175,
                            "MSFT": 0.004551883423966335
                        },
                        "99.0% EVaR": {
                            "AAPL": 0.0026204280588205692,
                            "CSCO": 0.01073094654162183,
                            "NFLX": 0.00579536539042559,
                            "CVX": 0.005481459347255648,
                            "PFE": 0.026486992061843014,
                            "MMM": 0.019769025494987304,
                            "MSFT": 0.006133926206208772
                        },
                        "99.9% EVaR": {
                            "AAPL": 0.0032907700492178886,
                            "CSCO": 0.013476072109692452,
                            "NFLX": 0.007277900565478697,
                            "CVX": 0.006883692984906125,
                            "PFE": 0.03326273349790646,
                            "MMM": 0.024826217526616574,
                            "MSFT": 0.007703069952849526
                        }
                    },
                    "CDaR": {
                        "90.0% CDaR": {
                            "AAPL": 0.009606895141541647,
                            "CSCO": 0.039341312137090405,
                            "NFLX": 0.02124670716501075,
                            "CVX": 0.020095878989866273,
                            "PFE": 0.09710541546692983,
                            "MMM": 0.07247630948749925,
                            "MSFT": 0.022487923555331253
                        },
                        "95.0% CDaR": {
                            "AAPL": 0.010071531076288585,
                            "CSCO": 0.04124404835619883,
                            "NFLX": 0.022274300731762755,
                            "CVX": 0.02106781293745795,
                            "PFE": 0.10180190323115731,
                            "MMM": 0.07598161451160809,
                            "MSFT": 0.02357554835269865
                        },
                        "99.0% CDaR": {
                            "AAPL": 0.010958454650511045,
                            "CSCO": 0.04487609977980065,
                            "NFLX": 0.02423582994402241,
                            "CVX": 0.022923095893942272,
                            "PFE": 0.1107668269545223,
                            "MMM": 0.08267274067776616,
                            "MSFT": 0.02565166860202774
                        },
                        "99.9% CDaR": {
                            "AAPL": 0.01154097818136238,
                            "CSCO": 0.0472615989152419,
                            "NFLX": 0.0255241449192955,
                            "CVX": 0.024141629271507533,
                            "PFE": 0.11665490927968279,
                            "MMM": 0.08706741295051432,
                            "MSFT": 0.027015245953290915
                        }
                    },
                    "EDaR": {
                        "90.0% EDaR": {
                            "AAPL": 0.010048950814352475,
                            "CSCO": 0.04115157965326437,
                            "NFLX": 0.02222436199442906,
                            "CVX": 0.0210205791324937,
                            "PFE": 0.10157366448342947,
                            "MMM": 0.07581126456729427,
                            "MSFT": 0.023522692232506092
                        },
                        "95.0% EDaR": {
                            "AAPL": 0.010500744725339062,
                            "CSCO": 0.04300172634601862,
                            "NFLX": 0.02322355401060491,
                            "CVX": 0.02196564989987255,
                            "PFE": 0.10614034651601191,
                            "MMM": 0.07921968683430124,
                            "MSFT": 0.024580256282424526
                        },
                        "99.0% EDaR": {
                            "AAPL": 0.01119591590799549,
                            "CSCO": 0.045848530238707726,
                            "NFLX": 0.024761001680204967,
                            "CVX": 0.023419821696075163,
                            "PFE": 0.11316705863453896,
                            "MMM": 0.08446419518363593,
                            "MSFT": 0.026207520469565256
                        },
                        "99.9% EDaR": {
                            "AAPL": 0.011601561760128647,
                            "CSCO": 0.04750969545918349,
                            "NFLX": 0.025658132179288504,
                            "CVX": 0.024268359109787477,
                            "PFE": 0.11726728127915773,
                            "MMM": 0.08752446740357454,
                            "MSFT": 0.0271570606465848
                        }
                    },
                    "VaR": {
                        "90.0% VaR": {
                            "AAPL": 0.0004797256854123439,
                            "CSCO": 0.0019645304390152893,
                            "NFLX": 0.0010609662130500268,
                            "CVX": 0.0010034989640607319,
                            "PFE": 0.004849013266595088,
                            "MMM": 0.003619145075780259,
                            "MSFT": 0.001122947048150095
                        },
                        "95.0% VaR": {
                            "AAPL": 0.0006501247679797108,
                            "CSCO": 0.0026623337767626453,
                            "NFLX": 0.001437822559991933,
                            "CVX": 0.0013599428819766012,
                            "PFE": 0.006571388025984055,
                            "MMM": 0.004904669322957229,
                            "MSFT": 0.0015218190547887148
                        },
                        "99.0% VaR": {
                            "AAPL": 0.0011671094857699787,
                            "CSCO": 0.004779444128549902,
                            "NFLX": 0.0025811912286243335,
                            "CVX": 0.0024413809715211274,
                            "PFE": 0.011797011400803296,
                            "MMM": 0.008804903878953657,
                            "MSFT": 0.0027319824469829177
                        },
                        "99.9% VaR": {
                            "AAPL": 0.0029072111133211214,
                            "CSCO": 0.011905355286227314,
                            "NFLX": 0.006429617715353408,
                            "CVX": 0.006081357386598929,
                            "PFE": 0.029385762918176354,
                            "MMM": 0.021932573353844954,
                            "MSFT": 0.006805231067098291
                        }
                    },
                    "DaR": {
                        "90.0% DaR": {
                            "AAPL": 0.008917372030201752,
                            "CSCO": 0.03651763772935586,
                            "NFLX": 0.019721750827473912,
                            "CVX": 0.01865352193256014,
                            "PFE": 0.0901357934179516,
                            "MMM": 0.06727441130083558,
                            "MSFT": 0.02087388043432375
                        },
                        "95.0% DaR": {
                            "AAPL": 0.009401962346935046,
                            "CSCO": 0.038502089378752824,
                            "NFLX": 0.020793475708711647,
                            "CVX": 0.019667196821403624,
                            "PFE": 0.09503397783074476,
                            "MMM": 0.07093025611362402,
                            "MSFT": 0.02200821466383251
                        },
                        "99.0% DaR": {
                            "AAPL": 0.010508602250072548,
                            "CSCO": 0.043033903790303224,
                            "NFLX": 0.023240931792353803,
                            "CVX": 0.02198208641384273,
                            "PFE": 0.10621976949217071,
                            "MMM": 0.07927896554880778,
                            "MSFT": 0.02459864926089857
                        },
                        "99.9% DaR": {
                            "AAPL": 0.01145957975347175,
                            "CSCO": 0.046928263231659134,
                            "NFLX": 0.025344123326928363,
                            "CVX": 0.023971358551076523,
                            "PFE": 0.11583214312660015,
                            "MMM": 0.08645332717517498,
                            "MSFT": 0.02682470763711701
                        }
                    },
                    "ERM": {
                        "90.0% ERM": {
                            "AAPL": 0.07833270410296742,
                            "CSCO": 0.3207812011324454,
                            "NFLX": 0.17324140640636868,
                            "CVX": 0.1638577833326516,
                            "PFE": 0.7917781618823924,
                            "MMM": 0.5909573511435581,
                            "MSFT": 0.1833620369324896
                        },
                        "95.0% ERM": {
                            "AAPL": 0.10191600860364712,
                            "CSCO": 0.417357475768082,
                            "NFLX": 0.22539848289433104,
                            "CVX": 0.2131897710814817,
                            "PFE": 1.0301555510264697,
                            "MMM": 0.7688744461619296,
                            "MSFT": 0.23856608995687595
                        },
                        "99.0% ERM": {
                            "AAPL": 0.15667474589405903,
                            "CSCO": 0.641600641144125,
                            "NFLX": 0.3465034641389202,
                            "CVX": 0.32773509941212975,
                            "PFE": 1.5836507080660016,
                            "MMM": 1.1819851476458316,
                            "MSFT": 0.36674593162585056
                        },
                        "99.9% ERM": {
                            "AAPL": 0.23501678768515066,
                            "CSCO": 0.9624200811558046,
                            "NFLX": 0.5197655218714718,
                            "CVX": 0.49161241549160795,
                            "PFE": 2.3755232542496114,
                            "MMM": 1.7730129441481053,
                            "MSFT": 0.5501298263192116
                        }
                    }
                }
            }
        }
    ]
}