def test_import_pipeline_modules():
    import scripts.data_generation.generate_data
    import scripts.ingestion.ingest_to_staging
    import scripts.transformation.staging_to_production
    import scripts.transformation.load_warehouse
    import scripts.quality_checks.validate_data