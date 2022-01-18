from ._patch_base import PatchBase


class Patch(PatchBase):
    name = 'Cleanup MAD DB for better performance'
    descr = 'Cleanup old data and rework db for better improvement'

    def _execute(self):
        self._logger.warning("This Patch may take a while if you don't clean your stats table often.")

        #Drop table trs_spawninsight because it is not used anymore
        drop_table_trs_spawnsightings = (
            "DROP TABLE IF EXISTS trs_spawnsightings;"
        )
        try:
            self._db.execute(drop_table_trs_spawnsightings, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table trs_stats_detect_raw because it is not used anymore, its split in https://github.com/Map-A-Droid/MAD/pull/877
        drop_table_trs_stats_detect_raw = (
            "DROP TABLE IF EXISTS trs_stats_detect_raw;"
        )
        try:
            self._db.execute(drop_table_trs_stats_detect_raw, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Note: Table below will drop very old tables, based on sample database. 
        #Drop table spawnpointdetectiondata because it is not used anymore (For the old mappers)
        drop_table_spawnpointdetectiondata = (
            "DROP TABLE IF EXISTS spawnpointdetectiondata;"
        )
        try:
            self._db.execute(drop_table_spawnpointdetectiondata, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table hashkeys because it is not used anymore (For the old mappers)
        drop_table_hashkeys = (
            "DROP TABLE IF EXISTS hashkeys;"
        )
        try:
            self._db.execute(drop_table_hashkeys, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table spawnpoint because it is not used anymore (For the old mappers)
        drop_table_spawnpoint = (
            "DROP TABLE IF EXISTS spawnpoint;"
        )
        try:
            self._db.execute(drop_table_spawnpoint, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table playerlocale because it is not used anymore (For the old mappers)
        drop_table_playerlocale = (
            "DROP TABLE IF EXISTS playerlocale;"
        )
        try:
            self._db.execute(drop_table_playerlocale, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table trainer because it is not used anymore
        drop_table_trainer = (
            "DROP TABLE IF EXISTS trainer;"
        )
        try:
            self._db.execute(drop_table_trainer, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table scanspawnpoint because it is not used anymore
        drop_table_scanspawnpoint = (
            "DROP TABLE IF EXISTS scanspawnpoint;"
        )
        try:
            self._db.execute(drop_table_scanspawnpoint, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table locationaltitude because it is not used anymore
        drop_table_locationaltitude = (
            "DROP TABLE IF EXISTS locationaltitude;"
        )
        try:
            self._db.execute(drop_table_locationaltitude, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Drop table mainworker because it is not used anymore
        drop_table_mainworker = (
            "DROP TABLE IF EXISTS mainworker;"
        )
        try:
            self._db.execute(drop_table_mainworker, commit=True)
        except Exception as e:
            self._logger.exception("Unexpected error: {}", e)
            self.issues = True

        #Problem: The trs_stats_detect_mon_raw primary key ID can run out of range 
        #Solution: Changing the Auto_Increment Value
        if not self._schema_updater.check_index_exists('trs_stats_detect_mon_raw', 'id'):
            alt_trs_stats_detect_mon_raw = (
                "ALTER TABLE `trs_stats_detect_mon_raw` MODIFY COLUMN `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT"
            )
            try:
                self._db.execute(alt_trs_stats_detect_mon_raw, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True

        # Add Indexes on trs_stats tables for queries performance, especially when there is alot of data. 
        # Not having indexes will typically result in high CPU usage in DB.
        # Note for indexing I use naming convention like Index IX and naming ix_tablename_col1_col2
        if not self._schema_updater.check_index_exists('trs_stats_detect', 'ix_trs_stats_detect_timestamp_scan'):
            add_index_trs_stats_detect = (
                "ALTER TABLE `trs_stats_detect`"
                "ADD INDEX ix_trs_stats_detect_timestamp_scan (`timestamp_scan`)"
            )
            try:
                self._db.execute(add_index_trs_stats_detect, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True

        if not self._schema_updater.check_index_exists('trs_stats_detect_mon_raw', 'ix_trs_stats_detect_mon_raw_timestamp_scan'):
            add_index_trs_stats_detect_mon_raw = (
                "ALTER TABLE `trs_stats_detect_mon_raw`"
                "ADD INDEX ix_trs_stats_detect_mon_raw_timestamp_scan (`timestamp_scan`)"
            )
            try:
                self._db.execute(add_index_trs_stats_detect_mon_raw, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True

        if not self._schema_updater.check_index_exists('trs_stats_detect_fort_raw', 'ix_trs_stats_detect_fort_raw_timestamp_scan'):
            add_index_trs_stats_detect_fort_raw = (
                "ALTER TABLE `trs_stats_detect_fort_raw`"
                "ADD INDEX ix_trs_stats_detect_fort_raw_timestamp_scan (`timestamp_scan`)"
            )
            try:
                self._db.execute(add_index_trs_stats_detect_fort_raw, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True

        if not self._schema_updater.check_index_exists('trs_stats_location', 'ix_trs_stats_location_timestamp_scan'):
            add_index_trs_stats_location = (
                "ALTER TABLE `trs_stats_location`"
                "ADD INDEX ix_trs_stats_location_timestamp_scan (`timestamp_scan`)"
            )
            try:
                self._db.execute(add_index_trs_stats_location, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True

        if not self._schema_updater.check_index_exists('trs_stats_location_raw', 'ix_trs_stats_location_raw_period'):
            add_index_trs_stats_location_raw = (
                "ALTER TABLE `trs_stats_location_raw`"
                "ADD INDEX ix_trs_stats_location_raw_period (`period`)"
            )
            try:
                self._db.execute(add_index_trs_stats_location_raw, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True

        # Feature: Column First_seen_timestamp in Pokestop table to have stats how many stops are added 
        if not self._schema_updater.check_column_exists('pokestop', 'first_seen_on'):
            add_column_first_seen_timestamp = (
                "ALTER TABLE `pokestop` "
                "ADD `first_seen_on` timestamp NOT NULL DEFAULT current_timestamp()"
            )
            try:
                self._db.execute(add_column_first_seen_timestamp, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True
        
        # Add index on time column to improve query performance
        if not self._schema_updater.check_index_exists('pokestop', 'ix_pokestop_first_seen_on'):
            add_index_pokestop_first_seen_on = (
                "ALTER TABLE `pokestop`"
                "ADD INDEX ix_pokestop_first_seen_on (`first_seen_on`)"
            )
            try:
                self._db.execute(add_index_pokestop_first_seen_on, commit=True)
            except Exception as e:
                self._logger.exception("Unexpected error: {}", e)
                self.issues = True        