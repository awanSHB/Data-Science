1. Scatter:
    fig = px.scatter(idv, x="lstat", y="medv", color="medv", size="medv",
                 hover_name="medv", title="Scatter Plot", trendline = 'ols')
    
    fig.update_layout(
        title_font=dict(size=20),
        title_x=0.5,
        title_y=0.9,
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(title='LSTAT'),
        yaxis=dict(title='MEDV')
    )

2. Seaborn:
    sns.set_style('darkgrid')
    sns.scatterplot(
        data=df,
        x='flipper_length_mm',
        y='body_mass_g',
        hue='species',
        style='sex'
    )
    plt.title('Flipper Length vs Body Mass')
    plt.xlabel('Flipper Length (mm)')
    plt.ylabel('Body Mass (g)')
    plt.show()