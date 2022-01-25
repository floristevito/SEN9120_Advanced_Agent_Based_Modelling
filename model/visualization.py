# define visualization elements
def vis(model, axs):
    # create axis
    ax1, ax2 = axs
    ax1.set_title('VTG capacity')
    ax2.set_title('total_current_power_demand')
    
    # VTG capacity plot on first axis
    data = model.output.variables.EtmEVsModel
    data['total_VTG_capacity'] = data['total_VTG_capacity'].astype(float)
    data['total_VTG_capacity'].plot(ax=ax1) 
    
    # Total current power demand on second axis
    data['total_current_power_demand'] = data['total_current_power_demand'].astype(float)
    data['total_current_power_demand'].plot(ax=ax2) 