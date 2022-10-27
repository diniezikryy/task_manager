import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { useRouter } from "next/router";
import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import Column from "../../../components/BoardPage/Column";
import AppLayout from "../../../components/hocs/AppLayout";

const BoardPage = () => {
  const [boardData, setBoardData] = useState({});
  const [columns, setColumns] = useState([]);
  const [tasks, setTasks] = useState([]);

  const router = useRouter();
  const loading = useSelector((state) => state.auth.loading);
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  const { board_id } = router.query;

  const fetchBoardData = async () => {
    const { data } = await axios.get(`/api/app/getBoard/${board_id}`, {
      method: "GET",
      headers: {
        Accept: "application/json",
      },
    });
    return data.board;
  };

  const { data } = useQuery(["boardData"], () => fetchBoardData());

  useEffect(() => {
    if (data) {
      setBoardData(data);
      setColumns(data.columns);
    }
  }, [data]);

  useEffect(() => {
    if (typeof window !== undefined && !loading && !isAuthenticated) {
      router.push("/login");
    }
  }, []);

  return (
    <AppLayout>
      <div className="flex py-6 pl-6">
        {columns.map((column) => (
          <Column column={column} key={column.id} />
        ))}
      </div>
    </AppLayout>
  );
};

export default BoardPage;
