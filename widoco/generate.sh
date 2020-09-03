#!/usr/bin/env bash

java -jar ./widoco-custom.jar \
    -ontFile ../roh-v2.owl \
    -oops \
    -webVowl \
    -includeAnnotationProperties \
    -outFolder output/roh \
    -rewriteAll \
    -confFile config-roh \
    -includeImportedOntologies \
    -uniteSections \
    -excludeIntroduction

java -jar ./widoco-custom.jar \
    -ontFile ../rohes-v2.owl \
    -oops \
    -webVowl \
    -includeAnnotationProperties \
    -outFolder output/rohes \
    -rewriteAll \
    -confFile config-rohes \
    -includeImportedOntologies \
    -uniteSections \
    -excludeIntroduction

java -jar ./widoco-custom.jar \
    -ontFile ../rohum.owl \
    -oops \
    -webVowl \
    -includeAnnotationProperties \
    -outFolder output/rohum \
    -rewriteAll \
    -confFile config-rohum \
    -includeImportedOntologies \
    -uniteSections \
    -excludeIntroduction