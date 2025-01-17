__version__ = "0.0.2"
import lazy_loader


__getattr__, __dir__, __all__ = lazy_loader.attach(
    __name__,
    submodules={
        'auto',
        'data',
        'help',
        'infra',
        'metrics',
        'nucleus',
    },
    submod_attrs={
        'auto': [
            'ComplexEncoder',
            'PostgresDatabaseConfig',
            'auto_exp_runs_path',
            'auto_run',
            'auto_run_running_path',
            'auto_try_decorator',
            'backbone_name2pe',
            'checkpoint_path',
            'command_executor',
            'database_config_path',
            'database_name',
            'delta_to_try',
            'end',
            'examples',
            'experiment',
            'fixed_meta_parameters',
            'full_finetune',
            'host',
            'infra',
            'learning_rate_exec',
            'learning_rates',
            'mutiple',
            'objective',
            'password',
            'peft_to_try',
            'port',
            'postgres_url',
            'run',
            'run_names',
            'run_with_config',
            'seed',
            'single',
            'sqlite_url',
            'start',
            'study',
            'study_path',
            'study_results',
            'username',
            'yuequ_to_try',
        ],
        'data': [
            'CIFAR100DataModule',
            'CIFAR10DataModule',
            'ClassificationDataConfig',
            'ClassificationDataModule',
            'Cub2011',
            'CutoutPIL',
            'DATA2CLS',
            'FashionMNISTDataModule',
            'KMNISTTDataModule',
            'MNISTDataModule',
            'MultiEpochsDataLoader',
            'NABirds',
            'PrefetchLoader',
            'QMNISTDataModule',
            'TorchVisionDataModule',
            'VtabDataset',
            'VtabSplit',
            'auto_augment_choices',
            'cls_names_of',
            'create_dataset',
            'create_loader',
            'create_transform',
            'cub2011',
            'dataloader_to_arrays',
            'dataset_factory',
            'dataset_name_choices',
            'dogs',
            'expand_to_chs',
            'fast_collate',
            'from_ssf',
            'get_continuous_class_map',
            'has_inaturalist',
            'has_places365',
            'infra',
            'load_class_names',
            'load_hierarchy',
            'loader',
            'nabirds',
            'simple_pixel_flatten_transform',
            'sksplit_for_torch',
            'stanford_dogs',
            'transforms',
            'transforms_direct_resize',
            'transforms_factory',
            'transforms_imagenet_eval',
            'transforms_imagenet_train',
            'transforms_simpleaug_train',
            'vtab',
            'vtab_1k',
        ],
        'help': [
            'lib_paths',
        ],
        'infra': [
            'memory',
        ],
        'metrics': [
            'compute_classification_metrics',
            'draw_classification_metrics',
            'except_roc_auc_score',
            'get_top_bottom_k_classes',
            'list_i_terms',
            'per_class_accuracy',
        ],
        'nucleus': [
            'ClassificationModelConfig',
            'ClassificationTask',
            'ClassificationTaskConfig',
            'HuggingfaceModel',
        ],
    },
)

__all__ = ['CIFAR100DataModule', 'CIFAR10DataModule',
           'ClassificationDataConfig', 'ClassificationDataModule',
           'ClassificationModelConfig', 'ClassificationTask',
           'ClassificationTaskConfig', 'ComplexEncoder', 'Cub2011',
           'CutoutPIL', 'DATA2CLS', 'FashionMNISTDataModule',
           'HuggingfaceModel', 'KMNISTTDataModule', 'MNISTDataModule',
           'MultiEpochsDataLoader', 'NABirds', 'PostgresDatabaseConfig',
           'PrefetchLoader', 'QMNISTDataModule', 'TorchVisionDataModule',
           'VtabDataset', 'VtabSplit', 'auto', 'auto_augment_choices',
           'auto_exp_runs_path', 'auto_run', 'auto_run_running_path',
           'auto_try_decorator', 'backbone_name2pe', 'checkpoint_path',
           'cls_names_of', 'command_executor',
           'compute_classification_metrics', 'create_dataset', 'create_loader',
           'create_transform', 'cub2011', 'data', 'database_config_path',
           'database_name', 'dataloader_to_arrays', 'dataset_factory',
           'dataset_name_choices', 'delta_to_try', 'dogs',
           'draw_classification_metrics', 'end', 'examples',
           'except_roc_auc_score', 'expand_to_chs', 'experiment',
           'fast_collate', 'fixed_meta_parameters', 'from_ssf',
           'full_finetune', 'get_continuous_class_map',
           'get_top_bottom_k_classes', 'has_inaturalist', 'has_places365',
           'help', 'host', 'infra', 'learning_rate_exec', 'learning_rates',
           'lib_paths', 'list_i_terms', 'load_class_names', 'load_hierarchy',
           'loader', 'memory', 'metrics', 'mutiple', 'nabirds', 'nucleus',
           'objective', 'password', 'peft_to_try', 'per_class_accuracy',
           'port', 'postgres_url', 'run', 'run_names', 'run_with_config',
           'seed', 'simple_pixel_flatten_transform', 'single',
           'sksplit_for_torch', 'sqlite_url', 'stanford_dogs', 'start',
           'study', 'study_path', 'study_results', 'transforms',
           'transforms_direct_resize', 'transforms_factory',
           'transforms_imagenet_eval', 'transforms_imagenet_train',
           'transforms_simpleaug_train', 'username', 'vtab', 'vtab_1k',
           'yuequ_to_try']
