from aiida.orm import Dict, load_node
from aiida.engine import submit

# import the FleurinpgenCalculation
from aiida_fleur.calculation.fleurinputgen import FleurinputgenCalculation

# load ingpen Code
inpgen_code = load_node(8)

# create a StuctureData


# create a parameters Dict
parameters = Dict(dict={
    'comp': {
        'kmax': 3.85
        },
    'atom': {
        'rmt' : 2.23
        }
    'kpt': {
        'div1': 12,
        'div2' : 10,
        'div3' : 1
        }})

# options

options = {'resources' : {"num_machines": 1, "num_mpiprocs_per_machine" : 1}, 'withmpi' : False}

# assemble inputs in a single dictionary

inputs = FleurinputgenCalculation.get_builder()
inputs.parameters = parameters
inputs.code = inpgen_code
inputs.structure = structure
inputs.metadata.options = options


# submit

inpgen_pk = submit(FleurinputgenCalculation, **inputs)
print('The PK of submitted inpgen job is'.format(res_pk)

