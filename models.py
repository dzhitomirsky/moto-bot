hd_query = {
    "min-year":2000,
    "currency":"USD",
    "sort[]":"creation_date",
    "page":1,
    "moto[0][17]":""
}

drag_star_query = {
    "min-year":2000,
    "min-capacity":1000,
    "drivetrain[]":2,
    "drivetrain[]":1,
    "currency":"USD",
    "sort[]":"creation_date",
    "page":1,
    "moto[0][59]":595
}

honda_vtx_query = {
    "min-year":2000,
    "min-capacity":1000,
    "max-capacity":1500,
    "drivetrain[]":1,
    "currency":"USD",
    "sort[]":"creation_date",
    "page":1,
    "moto[0][18]":280,
}

suzuki_bulevard_query = {
    "min-year":2000,
    "min-capacity":1000,
    "max-capacity":1500,
    "drivetrain[]":1,
    "currency":"USD",
    "sort[]":"creation_date",
    "page":1,
    "moto[0][49]":508,
    "moto[1][49]":515,
}

general = {
    "max-price":7000,
    "min-year":2000,
    "min-capacity":1000,
    "max-capacity":1800,
    "engine_configuration[]":1,
    "cylinder_count[]":2,
    "drivetrain[]":2,
    "drivetrain[]":1,
    "country":248,
    "region":349,
    "currency":"USD",
    "sort[]":"creation_date",
    "page":1,
    "type[0][1]":""
}


model_queries = {
    'Best lots in Minsk': general,
    'Yamaha DragStar 1100': drag_star_query,
    'Honda VTX 1300': honda_vtx_query,
    'Harley-Davidson': hd_query,
    'Suzuki Bulevard 1500': suzuki_bulevard_query
}
