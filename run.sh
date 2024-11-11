#!/bin/bash

docker run --rm --privileged -v /proc:/host_proc:ro -v /sys:/host_sys:ro amir-monitoring-agent
