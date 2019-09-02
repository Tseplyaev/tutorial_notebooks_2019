from aiida.orm import Dict, load_node
from aiida.engine import submit

# import the FleurinpgenCalculation
from aiida_fleur.calculation.fleur import FleurCalculation

# load Fleur Code
inpgen_code = load_node(8)

inpgen_calc_Fe = load_node(xxx)
inpgen_calc_Co = load_node(xxx)
inpgen_calc_Ni = load_node(xxx)

fleurinp_Fe = inpgen_calc_Fe.outputs.fleurinp
fleurinp_Co = inpgen_calc_Co.outputs.fleurinp
fleurinp_Ni = inpgen_calc_Ni.outputs.fleurinp

fleurinp_data_list = [fleurinp_Fe, fleurinp_Co, fleurinp_Ni]

options = Dict(dict={'resources' : {"num_mpiprocs_per_machine" : 2}})

calc_parameters = Dict(dict={
    'kpt': {
        'div1': 12,
        'div2' : 10,
        'div3' : 1
        }})

fleur_code = load_node(xxx)
inpgen_code = load_node(xxx)

for fleuinp in fleurinp_data_list:
    workchain_pk = submit(FleurSSDispWorkChain,
                          fleur=fleur_code,
                          calc_parameters=calc_parameters,
                          wf_parameters=wf_para,
                          fleurinp=fleurinp)
    print('Submitted SSDisp workchain pk={} for {} structure'.format(workchain_pk, structure.get_formula()))
