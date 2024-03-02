import { useEffect, useState } from "react";

function useFetch<Schema>(url: string) {
  const [state, setState] = useState<[Schema | null, boolean]>([null, false]);

  useEffect(() => {
    setState([null, true]);

    (async () => {
      const data = await fetch(url).then((res) => res.json()) as Schema;

      setState([data, false]);
    })();
  }, [url]);

  return state;
}

export default useFetch;
