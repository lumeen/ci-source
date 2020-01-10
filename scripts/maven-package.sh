#!/bin/bash
set -e

source ./ci-source/scripts/concourse-java.sh
setup_symlinks

cd project-source || echo "missing input resource: project-source"

echo "Using MAVEN_OPTS: ${MAVEN_OPTS}"

mvn clean package ${MAVEN_ARGS}

cd ..
cp project-source/target/*.zip maven-output/