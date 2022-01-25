# define visualization elements
def vis(model, axs):
    # create axis
    ax1, ax2 = axs
    ax1.set_title('VTG Capacity')
    ax2.set_title('Total Current Power Demand')
    
    # VTG capacity plot on first axis
    data = model.output.variables.EtmEVsModel
    data['total_VTG_capacity'] = data['total_VTG_capacity'].astype(float)
    data['total_VTG_capacity'].plot(ax=ax1) 
    ax1.set_xlabel('Time (15min)')
    ax1.set_ylabel('capacity (KW)')
    
    # Total current power demand on second axis
    data['total_current_power_demand'] = data['total_current_power_demand'].astype(float)
    data['total_current_power_demand'].plot(ax=ax2) 
    ax2.set_xlabel('Time (15min)')
    ax2.set_ylabel('capacity (KW)')