'''
this project is a demo of data analysis project. it visualizes variation in population of 10 Africa countries and also population trend of Nigeria over 10 years
'''

import os # essential for accessing system folders
import seaborn as sb # essential for plotting figures
import matplotlib.pyplot as plt # core data viuslization library
import numpy as np # for working wit arrays
import pandas as pd # for working with dataframes

year = np.arange(2015,2026)
nig_populations = np.array([190671878,196137826,200550927,205063323,209677248,214394986,219218873,224151298,229194702,234351583,239624493])

df = pd.DataFrame({'year':year,'population':nig_populations})
country_desnsity  = {
    'Nigeria':242431832,
    'Ethiopia':138902185,
    'Egypt':120101175,
    'Congo':116452162,
    'Tanzania':72563780,
    'South Africa':65453084,
    'Kenya':58636412,
    'Sudan':53282719,
    'Uganda':52761469,
    'Algeria':48028334
}
fig,axes = plt.subplots(1,2,figsize = (14,5))
dist_df = pd.DataFrame([country_desnsity])
sb.barplot(data=dist_df,ax=axes[0])
axes[0].tick_params(rotation=45)
axes[0].set_title('Africa Population distribution')
axes[1].set_title('Nigeria population trend')
sb.lineplot(x='year',y='population',data=df,ax=axes[1])
plt.show()


#save figure to device storage
try:
    desktop = os.path.join(os.path.expanduser("~"),"Desktop")
    file_location = os.path.join(desktop,'report.png')
    plt.savefig(file_location,dpi=300)

    import tkinter as tk
    from tkinter import messagebox
    win = tk.Tk()
    win.withdraw()
    messagebox.showinfo("File as been successfully save to 'Desktop' as 'report.png' ")


except:
    import tkinter as tk
    from tkinter import messagebox
    win = tk.Tk()
    win.withdraw()
    messagebox.showerror("File not saved!")
    


