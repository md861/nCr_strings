#Function to calculate all 
#the groups of indices generated
#by NCr for r \in {1,2,3,...,N}
# Arguments in: N
# Arguments out: 
# index_dict = {'length_list':[size(N+1) list of indices for each r \in {0,1,2,...,N}],
#               0:'NULL',
#               1:{'e1':['indices starting with 1'],...,'eN':['indices starting with N']},
#               2:{'e1':['indices starting with 1'],...,'eN':['indices starting with N']},
#               .:
#               .:
#               .:
#               N:{'e1':['indices starting with 1'],...,'eN':['indices starting with N']}}
#Example:-----------------------------
# Thus, the output can be accessed as:
# op = NCr_indices(N)
# op[length_list] = list of total indices for each r
# op[0] = 'NULL'
# dict_r = op[r]
# dict_r["e{}".format(i)] = list of groups for NCr,
#                           where each element within 
#                           the group starts with {i} 
# len(dict_r["e{}".format(i)])  == number of groups
#                                  that start with {i}
# sum(len(dict_r["e{}".format(i)])) over all i's == op[length_list][r]      
#--------------------------------------------------------------------------------------------
import copy

def NCr_indices(N):
    #define/initialize variables
    index_dict = dict()    #The output dictionary
    temp_dict = dict()     #To store indices for e{i}, i \in {1,2,3,...,N}
    N_list = list(range(1,N+1)) #Provides list for loops etc.
    for var0 in N_list:
        temp_dict["e{}".format(var0)] = list() 
        pass
    index_dict.update({"length_list":list(range(1,N+2))})
    index_dict["length_list"] = [0*vara for vara in index_dict["length_list"]]
    #update dictionary for r = 0
    index_dict.update({0:"NULL"})
    index_dict["length_list"][0] = 1
    #update dictionary for r = 1
    r=1
    er_dict = copy.deepcopy(temp_dict)
    count = 0   #counts the total number of entries in r-th index
    for var in N_list:
        er_dict["e{}".format(var)].append(str(var))
        count += 1
        pass
    index_dict.update({r:dict(er_dict)})
    index_dict["length_list"][r] = count
    #update dictionary for 2<=r<=N
    for r in list(range(2,N+1)):
        prev_dict = dict(index_dict[r-1]) #Get dictionary of entries for previous r
        er_dict = copy.deepcopy(temp_dict)
        count = 0   #counts the total number of entries in r-th index
        for rL_index in list(range(1,N+1-(r-1))):        
            for rR_index in list(range(rL_index+1,N+1-(r-2))):
                for i_sub in list(range(0,len(prev_dict["e{}".format(rR_index)]))):
                    er_dict["e{}".format(rL_index)].append(str(rL_index)+prev_dict["e{}".format(rR_index)][i_sub])
                    count += 1
                    pass
                pass
            pass
        index_dict.update({r:dict(er_dict)})
        index_dict["length_list"][r] = count
        pass 
        
    return index_dict
#Uncomment below for test
for var2 in list(range(4,5)):
    print('Total groups for N = ',var2,': ',sum(NCr_indices(var2)['length_list']))
    print('Lengh list for N = ',var2,': ',NCr_indices(var2)['length_list'])
    print('N = ',var2,': ',NCr_indices(var2))
    pass