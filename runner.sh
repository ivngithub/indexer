#!/bin/bash
start=$1
end=$2
way=$((end))-$((start))
cpu_count=$(grep -c ^processor /proc/cpuinfo)
cpu_count=$((cpu_count-2))
step=$(($((way))/$((cpu_count))))
echo "use CPU_COUNT=$cpu_count"
counter=$start
contact_id=$(python init_contract.py $((start)) $((end)) 2>&1)
docker build --tag indexer .
if (( $((way))>=200 ))
then
  for (( i=1; i <= $((cpu_count)); i++ ))
    do
      if (( $((counter-1+step))>=end ))
      then
        end_b=end
      else
        end_b=$((start+step))
      fi
      container_name="indexer_$((i))_start_$((start))_end_$((end_b))"
      echo "run: "$container_name
      docker run -d --name $container_name -e INDEXER_START_BLOCK=$((start)) -e INDEXER_END_BLOCK=$((end_b)) -e INDEXER_ID=$((i)) -e INDEXER_CONTACT_ID=$((contact_id)) -e POSTGRES_DB=indexer -e POSTGRES_USER=indexer -e POSTGRES_PASSWORD=indexer -e POSTGRES_HOST=db --link db indexer
      counter=$((counter+step+1))
      start=$((start+step+1))
    done
fi
