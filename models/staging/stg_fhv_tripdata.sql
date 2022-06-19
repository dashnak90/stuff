{{ config(materialized='view') }}


select 

    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropOff_datetime as timestamp) as dropOff_datetime,

from {{ source('staging','fhv_tripdata') }}