from re import X
from turtle import color
#steps involved in visulization
# step 1 labrarya layao
import seaborn as sns
import matplotlib.pyplot as plt


# step 2 theme per style ta color sato
sns.set_theme(style="ticks", color_codes="True")

# step 3 data la ao
jahaz = sns.load_dataset("titanic")

# # step 4 plot basic graph for 1 variable
p = sns.countplot(x="sex",data=jahaz,)
plt.show()

# step 5 with 2 variable with title
p = sns.countplot(x='sex',data=jahaz,hue="class")
# jab countplot ban gya to title dia so
p.set_title("ayaz ka count plot for jahaz")
plt.show()


