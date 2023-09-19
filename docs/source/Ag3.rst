Ag3 API
=======

This page provides a curated list of functions and properties available in the malariagen_data API relating to *Anopheles gambiae* data.

.. currentmodule:: malariagen_data.ag3

Basic data access
-----------------
.. autosummary::
    :toctree: generated/

    Ag3.client_location
    Ag3.config
    Ag3.lookup_release
    Ag3.open_file
    Ag3.read_files
    Ag3.releases
    Ag3.results_cache_get
    Ag3.results_cache_set
    Ag3.sample_sets

Sample metadata access
----------------------
.. autosummary::
    :toctree: generated/

    Ag3.add_extra_metadata
    Ag3.aim_metadata
    Ag3.clear_extra_metadata
    Ag3.cohorts_metadata
    Ag3.count_samples
    Ag3.general_metadata
    Ag3.lookup_sample
    Ag3.plot_samples_bar
    Ag3.plot_samples_interactive_map
    Ag3.sample_metadata
    Ag3.wgs_data_catalog

SNP data access
---------------
.. autosummary::
    :toctree: generated/

    Ag3.is_accessible
    Ag3.open_site_annotations
    Ag3.open_site_filters
    Ag3.open_snp_genotypes
    Ag3.open_snp_sites
    Ag3.plot_snps
    Ag3.plot_snps_track
    Ag3.site_annotations
    Ag3.site_filters
    Ag3.site_mask_ids
    Ag3.snp_allele_counts
    Ag3.snp_calls
    Ag3.snp_dataset
    Ag3.snp_genotypes
    Ag3.snp_sites
    Ag3.snp_variants

Haplotype data access
---------------------
.. autosummary::
    :toctree: generated/

    Ag3.haplotypes
    Ag3.open_haplotypes
    Ag3.open_haplotype_sites
    Ag3.phasing_analysis_ids
    

CNV data access
---------------
.. autosummary::
    :toctree: generated/

    Ag3.coverage_calls_analysis_ids
    Ag3.cnv_coverage_calls
    Ag3.cnv_discordant_read_calls
    Ag3.cnv_hmm
    Ag3.open_cnv_coverage_calls
    Ag3.open_cnv_discordant_read_calls
    Ag3.open_cnv_hmm
    Ag3.plot_cnv_hmm_coverage
    Ag3.plot_cnv_hmm_coverage_track
    Ag3.lot_cnv_hmm_heatmap
    Ag3.plot_cnv_hmm_heatmap_track
