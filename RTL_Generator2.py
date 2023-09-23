# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:24:08 2022

@author: dipay
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:14:30 2022

@author: haque
"""




def RTL_Generator2(line,c):
    
    from sva_parser2 import sva_parser2
   
    #print(filepath)
    #print('myline',line)
    #filename=filepath.split('/')[-1][0:-3]
    filename='C:\\Users\\dipay\\Downloads\\cad_project_final\\genarated_module_'+str(c)
    #filepath='C:/Users/dipay/Downloads/cad_project/sv_property1.sv'
    f = open(filename+'.v', 'w')
    #print('C:\\Users\\dipay\\Downloads\\cad_project\\'+filename+'.v')
    sens_type,sens_sig,dis_sig,dis_flag,assert_flag,assert_sign,consq_condition,ant_condition,inputlist,input_length=sva_parser2(line)
    
    
    #print(assert_sign)
    
    if assert_sign == '|=>':
        assert_sign = '<='
    elif assert_sign == '|->':
        assert_sign = '='
        
    
    #dis_sig="reset"
    count_tempantecedent=0;
    count_tempconsequent=0;
    count_ant_cond=0;
    count_consq_cond=0;
    
    ant_condition_lenght=len(ant_condition)
    
    
    print("\nmodule checker_auto( \n")
    f.write("\nmodule checker_auto( \n")
    #input declaration
    for x in range(len(inputlist)):
        if input_length[x]==1:
            print("\ninput wire %s," %inputlist[x]) 
            f.write("\ninput wire %s," %inputlist[x])
        else:
            print("\ninput wire [0:%d] %s," %(input_length[x]-1,inputlist[x])) 
            f.write("\ninput wire [0:%d] %s," %(input_length[x]-1,inputlist[x])) 
    #output declaration    
    print("\noutput wire pass);")
    f.write("\noutput wire pass);") 
     
    #register declaration
    ant_count=0;
    
    for y in range(len(ant_condition)):
        if y%2:
            ant_count=ant_count+int(ant_condition[y])
        else:
            ant_count=ant_count+1
            
    for y in range(0,ant_count):        
        print("\nreg tempantecedent%d;" %(y))
        f.write("\nreg tempantecedent%d;" %(y))
    for y in range(0,count_tempconsequent+1):
        print("\nreg tempconsequent%d;" %(y))
        f.write("\nreg tempconsequent%d;" %(y))
    
    print("\nreg pass_reg;")
    f.write("\nreg pass_reg;")
    
        
    
    #always block declaration    
    print("\nalways@(%s %s) \nbegin"%(sens_type,sens_sig))
    f.write("\nalways@(%s %s) \nbegin"%(sens_type,sens_sig))
    
    #disableif execution
    if dis_flag==0:
        f.write("\nif(%s)\n\tbegin\n\tpass_reg=1'b1;" %dis_sig)
        #print('dis_sig==',dis_sig)
        f.write("\n\ttempantecedent%d=0;" %(y))
    
        for y in range(0,ant_count):        
            print("\n\ttempantecedent%d=0;" %(y))
            f.write("\n\ttempantecedent%d=0;" %(y))
    
        for y in range(0,count_tempconsequent+1):
            print("\n\ttempconsequent%d=0;" %(y))
            f.write("\n\ttempantecedent%d=0;" %(y))
    
        print("\n\tend\nelse\n\tbegin\n" )
        f.write("\n\tend\nelse\n\tbegin\n" )
    
    
    
    
    if ant_condition_lenght>0:
        #1st antecedent condition
        print("\nif(%s) \n\tbegin\n\t\ttempantecedent0=1;\n\tend\nelse\n\tbegin\n\t\ttempantecedent0=0; \n\tend" %(ant_condition[0]))
        f.write("\nif(%s) \n\tbegin\n\t\ttempantecedent0=1;\n\tend\nelse\n\tbegin\n\t\ttempantecedent0=0; \n\tend" %(ant_condition[0]))
    
        for i in range(1,ant_condition_lenght):
            if i%2:
                #clock delay addition for ##clockcycles
                cycle=ant_condition[i]; 
                count_ant_cond=count_ant_cond+1; 
                for j in range(0,int(cycle)):
                    print("\nif(tempantecedent%d==1)\n\tbegin\n\t\ttempantecedent%d<=1;\n\tend\nelse\n\tbegin\n\t\ttempantecedent%d<=0;\n\tend"%(count_tempantecedent,(count_tempantecedent+1),(count_tempantecedent+1)))
                    f.write("\nif(tempantecedent%d==1)\n\tbegin\n\t\ttempantecedent%d<=1;\n\tend\nelse\n\tbegin\n\t\ttempantecedent%d<=0;\n\tend"%(count_tempantecedent,(count_tempantecedent+1),(count_tempantecedent+1)))
    
                    count_tempantecedent=count_tempantecedent+1
                    
            else:
                #2n antecedent condition
                count_ant_cond=count_ant_cond+1;               
                print("\nif(tempantecedent%d==1)\n\tbegin\n\tif(%s)\n\t\tbegin\n\t\t\ttempantecedent%d=1;\n\t\tend\n\telse\n\t\tbegin\n\t\t\ttempantecedent%d=0;\n\t\tend\n\tend\nelse\n\tbegin\n\t\ttempantecedent%d=0; \n\tend" %(count_tempantecedent,ant_condition[i],(count_tempantecedent+1),(count_tempantecedent+1),(count_tempantecedent+1)))
                f.write("\nif(tempantecedent%d==1)\n\tbegin\n\tif(%s)\n\t\tbegin\n\t\t\ttempantecedent%d=1;\n\t\tend\n\telse\n\t\tbegin\n\t\t\ttempantecedent%d=0;\n\t\tend\n\tend\nelse\n\tbegin\n\t\ttempantecedent%d=0; \n\tend" %(count_tempantecedent,ant_condition[i],(count_tempantecedent+1),(count_tempantecedent+1),(count_tempantecedent+1)))
    
                count_tempantecedent=count_tempantecedent+1
                
        #antecedent and conseq merge
        print("\nif(tempantecedent%d==1)\n\tbegin\n\t\ttempconsequent0%s1;\n\tend\nelse\n\tbegin\n\t\ttempconsequent0%s0; \n\tend" %(count_tempantecedent,assert_sign,assert_sign))            
        f.write("\nif(tempantecedent%d==1)\n\tbegin\n\t\ttempconsequent0%s1;\n\tend\nelse\n\tbegin\n\t\ttempconsequent0%s0; \n\tend" %(count_tempantecedent,assert_sign,assert_sign))            
    
    else:
        print("\ntempconsequent0=1;")    
        f.write("\ntempconsequent0=1;")    
     
    print("\nif(tempconsequent%d==1)\n\tbegin\n\tif(%s)\n\t\tbegin\n\t\t\tpass_reg=1;\n\t\tend\n\telse\n\t\tbegin\n\t\t\tpass_reg=0;\n\t\tend\n\tend\nelse\n\tbegin\n\t\tpass_reg=1; \n\tend" %(count_tempconsequent,consq_condition))
    f.write("\nif(tempconsequent%d==1)\n\tbegin\n\tif(%s)\n\t\tbegin\n\t\t\tpass_reg=1;\n\t\tend\n\telse\n\t\tbegin\n\t\t\tpass_reg=0;\n\t\tend\n\tend\nelse\n\tbegin\n\t\tpass_reg=1; \n\tend" %(count_tempconsequent,consq_condition))
    
    if dis_flag==0:
        print("\nend")
        f.write("\nend")
    
    print("\nend")  
    f.write("\nend")  
    
    
    print("\nassign pass=pass_reg;\n")      
    f.write("\nassign pass=pass_reg;\n")      
    
    
    print("\nendmodule\n")      
    f.write("\nendmodule\n")      
    
    f.close()