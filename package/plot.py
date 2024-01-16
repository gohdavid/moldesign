import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots

def rcparams():
    mpl.style.use('default')
    plt.style.use(['science', 'nature', 'no-latex'])
    plt.rcParams.update({
        'figure.figsize': (3, 2),
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'ytick.right': False,
        'xtick.top': False,
        'xtick.minor.visible': False,
        'ytick.minor.visible': False,
        'axes.grid': False,
        'axes.spines.right': False,
        'axes.spines.top': False,
        "font.family": "sans-serif",
        'font.sans-serif': 'MLMSans10',
        'figure.dpi': 300,
    })

    plt.rcParams['figure.facecolor'] = 'white'

sns.lineplot(x=[0,1],y=[0,1])
rcparams()
plt.close()
    
