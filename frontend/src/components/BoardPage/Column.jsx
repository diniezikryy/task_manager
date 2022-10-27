import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import React, { useEffect, useState } from "react";

const Column = ({ column }) => {
  const [tasks, setTasks] = useState(column.tasks);

  const fetchColumnTasks = async () => {
    const { data } = await axios.get(`/api/app/getColumn/${column.id}`, {
      method: "GET",
      headers: {
        Accept: "application/json",
      },
    });

    return data.column;
  };

  const { data } = useQuery(["columnTasks", column.id], () =>
    fetchColumnTasks()
  );

  useEffect(() => {
    if (data) {
      setTasks(data.tasks);
    }
  }, [data]);

  return (
    <div className="mr-6 w-72">
      <h1 className="text-sm font-normal text-grey-light-tertiary">
        {column.name}
      </h1>

      <div>
        {tasks.map((task) => (
          <div>{task.title}</div>
        ))}
      </div>
    </div>
  );
};

export default Column;
