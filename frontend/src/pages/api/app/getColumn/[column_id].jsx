import cookie from "cookie";
import { API_URL } from "../../../../config/index";

export default async (req, res) => {
  const { column_id } = req.query;

  if (req.method === "GET") {
    const cookies = cookie.parse(req.headers.cookie ?? "");
    const access = cookies.access ?? false;

    if (access === false) {
      return res.status(401).json({
        error: "User unauthorised to make this request",
      });
    }

    try {
      const apiRes = await fetch(
        `${API_URL}/api/account/columns/${column_id}`,
        {
          method: "GET",
          headers: {
            Accept: "application/json",
            Authorization: `Bearer ${access}`,
          },
        }
      );

      const data = await apiRes.json();

      if (apiRes.status === 200) {
        return res.status(200).json({
          column: data.column,
        });
      } else {
        return res.status(apiRes.status).json({
          error: data.error,
        });
      }
    } catch (err) {
      return res.status(500).json({
        error: "Something went wrong when retrieving boards",
      });
    }
  } else {
    res.setHeader("Allow", ["GET"]);
    return res.status(405).json({
      error: `Method ${req.method} not allowed`,
    });
  }
};
