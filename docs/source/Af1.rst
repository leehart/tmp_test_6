Af1 API
=======

This page provides a curated list of functions and properties available in the malariagen_data API relating to *Anopheles funestus* data.

.. currentmodule:: malariagen_data.af1

Basic data access
-----------------
.. autosummary::
    :toctree: generated/

    Af1.client_location
    Af1.config
    Af1.lookup_release
    Af1.open_file
    Af1.read_files
    Af1.releases
    Af1.results_cache_get
    Af1.results_cache_set
    Af1.sample_sets

Sample metadata access
----------------------
.. autosummary::
    :toctree: generated/

    Af1.add_extra_metadata
    Af1.aim_metadata
    Af1.clear_extra_metadata
    Af1.cohorts_metadata
    Af1.count_samples
    Af1.general_metadata
    Af1.lookup_sample
    Af1.plot_samples_bar
    Af1.plot_samples_interactive_map
    Af1.sample_metadata
    Af1.wgs_data_catalog

SNP data access
---------------
.. autosummary::
    :toctree: generated/

    Af1.is_accessible
    Af1.open_site_annotations
    Af1.open_site_filters
    Af1.open_snp_genotypes
    Af1.open_snp_sites
    Af1.plot_snps
    Af1.plot_snps_track
    Af1.site_annotations
    Af1.site_filters
    Af1.site_mask_ids
    Af1.snp_allele_counts
    Af1.snp_calls
    Af1.snp_dataset
    Af1.snp_genotypes
    Af1.snp_sites
    Af1.snp_variants

Haplotype data access
---------------------
.. autosummary::
    :toctree: generated/

    Af1.haplotypes
    Af1.open_haplotypes
    Af1.open_haplotype_sites
    Af1.phasing_analysis_ids
    

CNV data access
---------------
.. autosummary::
    :toctree: generated/

    Af1.coverage_calls_analysis_ids
    Af1.cnv_coverage_calls
    Af1.cnv_discordant_read_calls
    Af1.cnv_hmm
    Af1.open_cnv_coverage_calls
    Af1.open_cnv_discordant_read_calls
    Af1.open_cnv_hmm
    Af1.plot_cnv_hmm_coverage
    Af1.plot_cnv_hmm_coverage_track
    Af1.plot_cnv_hmm_heatmap
    Af1.plot_cnv_hmm_heatmap_track
