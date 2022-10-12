import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { request_refresh } from "../actions/auth";
import Head from "next/head";

const Layout = ({ title, content, children }) => {
  const dispatch = useDispatch();

  useEffect(() => {
    if (dispatch && dispatch !== null && dispatch !== undefined)
      dispatch(request_refresh());
  }, [dispatch]);

  return (
    <>
      <Head>
        <title>{title}</title>
        <meta name="description" content={content} />
      </Head>

      <div className="">{children}</div>
    </>
  );
};

Layout.defaultProps = {
  title: "Kanban App | ",
  content: "Kanban Task Manager",
};

export default Layout;
