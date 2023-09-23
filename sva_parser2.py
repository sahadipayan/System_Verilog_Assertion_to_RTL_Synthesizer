# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:16:29 2022

@author: dipay
"""

def sva_parser2(line): 
    import numpy as np
    import re
    #read input files
    input_list=[]

    target_line=re.sub('[@,;,(,)]', '', line)
    target_line=re.sub('&&', ' && ', target_line)
    target_line=re.sub('>', '> ', target_line)
    target_line=target_line.replace('^',' ^ ')
    target_line=re.sub('==', ' == ', target_line)
    target_line=re.sub('!=', ' != ', target_line)
    target_line=re.sub('iff', 'iff ', target_line)
    target_line=re.sub('[.]', '_', target_line)

     
    for j in range(len(target_line)):
         if target_line[j]=='>':
             target_line=target_line[0:j-2]+' '+target_line[j-2:j+1]+' '+target_line[j+1:]
             break
         
    target_line=target_line.split()
             #print(target_line)
            
            
    
    sens_sign= []
    sens_type= []
    length_inputs=[]
    
    
    if target_line[0]=='posedge' or 'negedge':
        sens_sign= target_line[1]
        input_list.append(target_line[1])
        length_inputs.append([target_line[1],1])
    
        sens_type= target_line[0]
      
    print('sens_type:',  sens_type)
    print('sens_sign:', sens_sign)
      
    target_line.remove(sens_type)
    target_line.remove(sens_sign)
    
    
  
    assert_sign=[]
    dis_sig=[]
    dis_flag=1
    location_reset=0
    
        
    if "disable" in target_line:
    
        dis_flag=0
        input_list.append(target_line[2])
        dis_sig=target_line[2]
        length_inputs.append([target_line[2],1])
        location_reset=2
            
    if dis_flag==0:
        target_line=target_line[location_reset+1:]    
    
    assert_flag=0
    if '|->' in target_line:
          assert_sign='|->'
          assert_flag=1
    elif '|=>' in target_line:
          assert_sign='|=>'
          assert_flag=1
    else:  
          assert_sign=[]
          
          
          
    print('assert_sign:',assert_sign)
    
    
    if assert_flag==1:
        location_assert_sign=target_line.index(assert_sign)
        consequent_list=target_line[location_assert_sign+1:]
        antecedent_list=target_line[0:location_assert_sign]
    else:
        consequent_list=target_line
        antecedent_list=[]
        
    count_antecedent=0
    antecedent_values=[]
    locations_antecedent=[]
    
    
    for i in range(len(antecedent_list)):
        item=antecedent_list[i]
        if "##" in item:
            antecedent_values.append(item[2:])
            count_antecedent=count_antecedent+1
            locations_antecedent.append(i)
            item=re.sub('##', '', item)        
            antecedent_list[i]=item
      
            
    locations_antecedent.append(len(antecedent_list))
    #print('antecedent_list:', antecedent_list )
    antecedent_list_temp=[]
    temp=[]
    prev=0
    antecedent_list_final=[]
    if len(antecedent_list)>0:
        for i in range(0,len(locations_antecedent)):
        #print(i)
            temp=" ".join(antecedent_list[prev:locations_antecedent[i]])
            prev=locations_antecedent[i]+1
        #print(temp)
            antecedent_list_temp.append(temp)
    
    
    
        
        for i in range(len(antecedent_list_temp)-1):
            antecedent_list_final.append(antecedent_list_temp[i])
            antecedent_list_final.append(antecedent_values[i])
            
        
        antecedent_list_final.append(antecedent_list_temp[-1])
    
      
    
    count_consequent=0
    consequent_values=[]
    locations_consequent=[]
    
    
    for i in range(len(consequent_list)):
        item=consequent_list[i]
        if "##" in item:
            consequent_values.append(item[2:])
            count_consequent=count_consequent+1
            locations_consequent.append(i)
            item=re.sub('##', '', item)        
            consequent_list[i]=item
      
            
    locations_consequent.append(len(consequent_list))
    #print('antecedent_list:', antecedent_list )
    consequent_list_temp=[]
    temp=[]
    prev=0
    consequent_list_final=[]
    if len(consequent_list)>0:
        for i in range(0,len(locations_consequent)):
        #print(i)
            temp=" ".join(consequent_list[prev:locations_consequent[i]])
            prev=locations_consequent[i]+1
        #print(temp)
            consequent_list_temp.append(temp)
    
    
    
        
        for i in range(len(consequent_list_temp)-1):
            consequent_list_final.append(consequent_list_temp[i])
            consequent_list_final.append(consequent_values[i])
            
        
        consequent_list_final.append(consequent_list_temp[-1])
    
      
        
    
    #consequent_list_final= " ".join(consequent_list)
    #consequent_list_final= list(consequent_list_final)
    #consequent_list_final= consequent_list
    
    #consequent_list_final=[]
    #for i in range(len(consequent_list_temp)-1):
    #    consequent_list_final.append(consequent_list_temp[i])
    #    consequent_list_final.append(consequent_values[i])
        
    #consequent_list_final.append(consequent_list_temp[-1])
    
     
    print('consequent_list:', consequent_list_final )
    print('antecedent_list:', antecedent_list_final )
    
     
    print('consequent_list:', consequent_list )
    print('antecedent_list:', antecedent_list )
    
    arrays=[]
    delete_items=[]
    for i in range(len(antecedent_list)):
        item=antecedent_list[i]
        if "==" in item:
           delete_items.append(antecedent_list[i])
         
        if "&&" in item:
           delete_items.append(antecedent_list[i])
        if "||" in item:
           delete_items.append(antecedent_list[i])
        if "^" in item:
           delete_items.append(antecedent_list[i])
        if "!=" in item:
           delete_items.append(antecedent_list[i])
        if "'" in item:
           delete_items.append(antecedent_list[i])
           length_inputs.append([antecedent_list[i-2],int(item[0])])
           #print(antecedent_list)
           #dictOfWords1 = dict.fromkeys(antecedent_list[i-2],int(item[0]))
           #listofTuples=[(antecedent_list[i-2],int(item[0]))]
           #arrays.append([antecedent_list[i-2],int(item[0])])
    
    
    
    
    for i in range(len(delete_items)):
        antecedent_list.remove(delete_items[i])    
        
    for i in range(len(antecedent_list)):  
        if len(antecedent_list[i])>1:
            input_list.append(antecedent_list[i])    
    
            
    delete_items=[]
    for i in range(len(consequent_list)):
        item=consequent_list[i]
        if "=="  in item:
           #print(consequent_list[i+1])
          
    
           delete_items.append(consequent_list[i])
        if "&&"  in item:
           delete_items.append(consequent_list[i])
        if "||" in item:
           delete_items.append(consequent_list[i])
          
        if "^" in item:
           delete_items.append(consequent_list[i])
          
        if "!=" in item:
           delete_items.append(consequent_list[i])
           
        if "'" in item:
           delete_items.append(consequent_list[i])
         
           length_inputs.append([consequent_list[i-2],int(item[0])])
           
           #dictOfWords = dict.fromkeys(consequent_list[i-1],int(item[0]))
         
    
    for i in range(len(delete_items)):
        consequent_list.remove(delete_items[i])   
        
        
    for i in range(len(consequent_list)):   
        if len(consequent_list[i])>1:
            input_list.append(consequent_list[i])      
    
    
    
    
    input_list_final=[]
    
    [input_list_final.append(x) for x in input_list if x not in input_list_final]
    
    length_inputs_reduced=[]
    [length_inputs_reduced.append(x) for x in length_inputs if x not in length_inputs_reduced]
    
    print('input list:', input_list_final)
    #print('input list final:', input_list_final)
    #print('input list length:', length_inputs)
    
    input_length_final=[]
    
    length_inputs=np.array(length_inputs)
    count=0
    for i in input_list_final:
        print(i)
        if i in length_inputs[:,0]:
            
            #input_length_final.append(int(length_inputs_reduced[input_list_final.index(i)][1]))
            input_length_final.append(int(length_inputs_reduced[count][1]))
            count=count+1
        else:
            input_length_final.append(1)
    
    print('input length:', input_length_final)
    
    
    return sens_type,sens_sign, dis_sig,dis_flag,assert_flag,assert_sign,consequent_list_final,antecedent_list_final,input_list_final,input_length_final
           
    
    
    
