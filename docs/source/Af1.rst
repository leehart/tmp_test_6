Af1 API
=======

This page provides a curated list of functions and properties available in the malariagen_data API relating to *Anopheles funestus* data.

Basic data access
-----------------
.. autosummary::
    :toctree: generated/

    malariagen_data.af1.Af1.client_location
    malariagen_data.af1.Af1.config
    malariagen_data.af1.Af1.lookup_release
    malariagen_data.af1.Af1.open_file
    malariagen_data.af1.Af1.read_files
    malariagen_data.af1.Af1.releases
    malariagen_data.af1.Af1.results_cache_get
    malariagen_data.af1.Af1.results_cache_set
    malariagen_data.af1.Af1.sample_sets

Sample metadata access
----------------------
.. autosummary::
    :toctree: generated/

    malariagen_data.af1.Af1.add_extra_metadata
    malariagen_data.af1.Af1.aim_metadata
    malariagen_data.af1.Af1.clear_extra_metadata
    malariagen_data.af1.Af1.cohorts_metadata
    malariagen_data.af1.Af1.count_samples
    malariagen_data.af1.Af1.general_metadata
    malariagen_data.af1.Af1.lookup_sample
    malariagen_data.af1.Af1.plot_samples_bar
    malariagen_data.af1.Af1.plot_samples_interactive_map
    malariagen_data.af1.Af1.sample_metadata
    malariagen_data.af1.Af1.wgs_data_catalog

SNP data access
---------------
.. autosummary::
    :toctree: generated/

    malariagen_data.af1.Af1.is_accessible
    malariagen_data.af1.Af1.open_site_annotations
    malariagen_data.af1.Af1.open_site_filters
    malariagen_data.af1.Af1.open_snp_genotypes
    malariagen_data.af1.Af1.open_snp_sites
    malariagen_data.af1.Af1.plot_snps
    malariagen_data.af1.Af1.plot_snps_track
    malariagen_data.af1.Af1.site_annotations
    malariagen_data.af1.Af1.site_filters
    malariagen_data.af1.Af1.site_mask_ids
    malariagen_data.af1.Af1.snp_allele_counts
    malariagen_data.af1.Af1.snp_calls
    malariagen_data.af1.Af1.snp_dataset
    malariagen_data.af1.Af1.snp_genotypes
    malariagen_data.af1.Af1.snp_sites
    malariagen_data.af1.Af1.snp_variants

Haplotype data access
---------------------
.. autosummary::
    :toctree: generated/

    malariagen_data.af1.Af1.haplotypes
    malariagen_data.af1.Af1.open_haplotypes
    malariagen_data.af1.Af1.open_haplotype_sites
    malariagen_data.af1.Af1.phasing_analysis_ids
    

CNV data access
---------------
.. autosummary::
    :toctree: generated/

    malariagen_data.af1.Af1.coverage_calls_analysis_ids
    malariagen_data.af1.Af1.cnv_coverage_calls
    malariagen_data.af1.Af1.cnv_discordant_read_calls
    malariagen_data.af1.Af1.cnv_hmm
    malariagen_data.af1.Af1.open_cnv_coverage_calls
    malariagen_data.af1.Af1.open_cnv_discordant_read_calls
    malariagen_data.af1.Af1.open_cnv_hmm
    malariagen_data.af1.Af1.plot_cnv_hmm_coverage
    malariagen_data.af1.Af1.plot_cnv_hmm_coverage_track
    malariagen_data.af1.Af1.plot_cnv_hmm_heatmap
    malariagen_data.af1.Af1.plot_cnv_hmm_heatmap_track
