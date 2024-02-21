
def temp_conv(source_val ,conv_type):

    if conv_type=='C':
        conv_val = float(source_val - 32 ) * 5 /9
    else:
        conv_val = float(source_val) * 9 / 5 + 32
    return conv_val


def speed_conv(source_val ,conv_type):
    if conv_type == 'MPH':
        conv_val = float(source_val ) /1.609
    else:
        conv_val = float(source_val ) *1.609
    return conv_val

def weight_conv(source_val,source_type ,conv_type):
    if source_type=='kg':
        if conv_type=='stone':
            conv_val = float(source_val)/6.35
        else:
            conv_val=float(source_val)*2.205
    elif source_type=='stone':
        if conv_type == 'lbs':
            conv_val = source_val * 14
        else:
            conv_val = float(source_val) *6.35
    else :
        if conv_type == 'stone':
            conv_val = source_val/14
        else:
            conv_val = float(source_val) / 2.205
    return conv_val


if __name__ == '__main__':

    source_val,source_type,conv_type,=input("Enter your conversion info(value,source,conv):").split()
    source_val=float(source_val)
    if source_type in {'C','F'}:
        conv_val=temp_conv(source_val,conv_type)
    elif source_type in {'MPH','KPH'}:
        conv_val = speed_conv(source_val, conv_type)
    else:
        conv_val = weight_conv(source_val, source_type, conv_type)
    print("Conversion value is :"+str(conv_val))

