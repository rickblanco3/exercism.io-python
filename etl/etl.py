def transform(legacy):
    return {ltr.lower():pts for pts,ltrs in legacy.iteritems() for ltr in ltrs}
