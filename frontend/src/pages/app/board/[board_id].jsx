import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { useRouter } from "next/router";
import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import AppLayout from "../../../components/hocs/AppLayout";

const BoardPage = () => {
  const [boardData, setBoardData] = useState({});
  const [columns, setColumns] = useState([]);

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
    return data;
  };

  const { data } = useQuery(["boardData"], () => fetchBoardData());

  useEffect(() => {
    if (data) {
      setBoardData(data.board[0]);
      setColumns(data.board[0].columns);
    }
  }, [data]);

  useEffect(() => {
    if (typeof window !== undefined && !loading && !isAuthenticated) {
      router.push("/login");
    }
  }, []);

  return (
    <AppLayout>
      <div className="flex p-6">
        {columns.map((column) => (
          <div className="w-1/3">{column.name}</div>
        ))}
      </div>
    </AppLayout>
  );
};

export default BoardPage;
