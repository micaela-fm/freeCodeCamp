import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('./medical_examination.csv')

# 2
weight_kg = df['weight']
height_m = df['height'] / 100
bmi = weight_kg / np.power(height_m, 2)
df['overweight'] = (bmi > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['id', 'cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    cat_plot = sns.catplot(
        data=df_cat, 
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        kind='bar'
    )


    # 8
    fig = cat_plot.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    clean_pressure = df['ap_lo'] <= df['ap_hi']
    clean_height = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    clean_weight = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))

    df_heat = df[clean_pressure & clean_height & clean_weight]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(
        corr,
        center=0,
        annot=True,  # Annotate with correlation coefficients
        fmt=".1f",  # Format for annotations
        cbar_kws={"shrink": .8},  # Colorbar size
        square=True,  # Aspect ratio 1:1
        mask=mask,
        ax=ax  # Pass the axes to the heatmap function
    )

    # 16
    fig.savefig('heatmap.png')
    return fig
