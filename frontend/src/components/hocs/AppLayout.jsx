import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { request_refresh, logout } from "../../actions/auth";
import Head from "next/head";
import { useRouter } from "next/router";
import Drawer from "../AppLayout/Drawer";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import Navbar from "../AppLayout/Navbar";

const AppLayout = ({ title, content, children }) => {
  const [userBoards, setUserBoards] = useState([]);
  const [showSidebar, setShowSidebar] = useState(true);

  const board = useSelector((state) => state.auth.board);

  const dispatch = useDispatch();

  const fetchBoardData = async () => {
    const { data } = await axios.get("/api/app/getUserBoards", {
      method: "GET",
      headers: {
        Accept: "application/json",
      },
    });
    return data;
  };

  useEffect(() => {
    if (dispatch && dispatch !== null && dispatch !== undefined)
      dispatch(request_refresh());
  }, [dispatch]);

  const { data } = useQuery(["userboards"], () => fetchBoardData());

  useEffect(() => {
    if (data) {
      setUserBoards([...data.boards]);
    }
  }, [data]);

  return (
    <>
      <Head>
        <title>{title}</title>
        <meta name="description" content={content} />
      </Head>

      <div className="flex w-screen h-screen">
        <Drawer
          userBoards={userBoards}
          showSidebar={showSidebar}
          setShowSidebar={setShowSidebar}
        />
        <div className="flex flex-col w-full">
          <Navbar showSidebar={showSidebar} board={board} />

          <div className="h-full bg-grey-light-secondary">{children}</div>
        </div>
      </div>
    </>
  );
};

AppLayout.defaultProps = {
  title: "Kanban App | ",
  content: "Kanban Task Manager",
};

export default AppLayout;
