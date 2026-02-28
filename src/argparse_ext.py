def build_filters_from_argv(args):
    filters = {}
    active_key = None
    argv = args._argv

    i = 0
    while i < len(argv):
        token = argv[i]

        if token == "--key":
            active_key = argv[i + 1]
            i += 2
            continue

        if token == "--min":
            filters[f"min_{active_key}"] = int(argv[i + 1])
            i += 2
            continue

        if token == "--max":
            filters[f"max_{active_key}"] = int(argv[i + 1])
            i += 2
            continue

        if token == "--equals":
            filters[f"eq_{active_key}"] = argv[i + 1]
            i += 2
            continue

        if token == "--not-equals":
            filters[f"not_eq_{active_key}"] = argv[i + 1]
            i += 2
            continue

        if token == "--contains":
            filters[f"contains_{active_key}"] = argv[i + 1]
            i += 2
            continue

        if token == "--not-contains":
            filters[f"not_contains_{active_key}"] = argv[i + 1]
            i += 2
            continue

        if token == "--regex":
            filters[f"regex_{active_key}"] = argv[i + 1]
            i += 2
            continue

        if token == "--not-regex":
            filters[f"not_regex_{active_key}"] = argv[i + 1]
            i += 2
            continue

        i += 1

    return filters