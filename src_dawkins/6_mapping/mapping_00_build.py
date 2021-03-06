ds = ds
model_search = model_search
ds.dtypes()
ds.search_grid

#%% Build feature and model variables
vset_feature = gamete.design_space.VariableList("feature set", list())
vset_model = gamete.design_space.VariableList("model set", list())

# Ensure no overlap in columns!
feature_names = [vdef['name'] for vdef in ds.search_grid]
hyper_param_names = [vdef['name'] for vdef in model_search.search_grid]
assert not list(set(feature_names) & set(hyper_param_names))

# Build the variable sets
for vdef in ds.search_grid:
    vset_feature.append(gamete.design_space.Variable(**vdef))

for vdef in model_search.search_grid:
    vset_model.append(gamete.design_space.Variable(**vdef))

#%% Create the DesignSpace
this_ds = gamete.design_space.DesignSpace([vset_feature, vset_model])
print(this_ds)

this_ds.print_design_space()
print(this_ds)
#%% Create a single Genome

for i in range(20):
    genes = this_ds.gen_genes()

    this_genome = gamete.evolution_space.Genome(genes)
    # this_genome.print_genes()
    logging.info("Genome: {}".format(this_genome))

    run_definition = dict()
    run_definition['generation'] = 0
    run_definition['population_number'] = i
    run_definition['id'] = this_genome.hash
    run_definition['path_data_root'] = PATH_DATA_ROOT
    run_definition['genome'] = this_genome.export_genome()
    run_definition['sample fraction'] = 0.5
    run_definition['random seed'] = 42
    run_definition['cv folds'] = 5

    type(run_definition['genome'])

    out_file_name = "control {}.json".format(run_definition['id'])
    out_folder_name ="{:03d}_{}".format(run_definition['population_number'],run_definition['id'])
    out_path = Path(PATH_EXPERIMENT_ROOT).expanduser() / str(run_definition['generation']) / out_folder_name / out_file_name

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w') as f:
        yaml.dump(run_definition, f, default_flow_style=False)
    logging.info("Wrote run definition to {}".format(out_file_name))

